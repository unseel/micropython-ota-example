import ubluetooth as bt
import struct
from . import ble_tools
from . import ble_const
from . import ota_controller

PACK = struct.pack
BLETools = ble_tools.BLETools
BLEConst = ble_const.BLEConst

class GenericAccess(object):
	UUID = bt.UUID("5E400001-B5A3-F393-E0A9-E50E24DCCA9E")

	__DEVICE_NAME_CHAR = (bt.UUID("5E400002-B5A3-F393-E0A9-E50E24DCCA9E"), bt.FLAG_READ,)
	__APPEARANCE_CHAR = (bt.UUID("5E400003-B5A3-F393-E0A9-E50E24DCCA9E"), bt.FLAG_READ,)
	__PERIPHERAL_PREFERRED_CONNECTION_PARAMETERS = (bt.UUID("5E400004-B5A3-F393-E0A9-E50E24DCCA9E"), bt.FLAG_READ,)
	__CENTRAL_ADDRESS_RESOLUTION = (bt.UUID("5E400005-B5A3-F393-E0A9-E50E24DCCA9E"), bt.FLAG_READ | bt.FLAG_WRITE)

	SERVICE = (
		UUID,
		(
			__DEVICE_NAME_CHAR,
			__APPEARANCE_CHAR,
			__PERIPHERAL_PREFERRED_CONNECTION_PARAMETERS,
			__CENTRAL_ADDRESS_RESOLUTION
		)
	)

	class Values(object):
		DEVICE_NAME = PACK("<6s", "abcdef".encode())
		APPEARANCE = PACK("<h", 961)
		PERIPHERAL_PREFERRED_CONNECTION_PARAMETERS = PACK("<4h", 40, 80, 10, 300)
		CENTRAL_ADDRESS_RESOLUTION = PACK("<b", 1)

class UartService(object):
	UUID = bt.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
	__RX_UUID = (bt.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"), bt.FLAG_WRITE | bt.FLAG_READ,)
	__TX_UUID = (bt.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"), bt.FLAG_NOTIFY | bt.FLAG_READ,)

	SERVICE = (
		UUID,
		(
			__TX_UUID,
			__RX_UUID
		)
	)

	class Values(object):
		RX_VALUE = PACK("<8s", "rx ready".encode())
		TX_VALUE = PACK("<8s", "tx ready".encode())


class OtaService(object):
	UUID = bt.UUID("3E400001-B5A3-F393-E0A9-E50E24DCCA9E")
	
	__OTA_FLAG_CHAR = (bt.UUID("3E400002-B5A3-F393-E0A9-E50E24DCCA9E"), bt.FLAG_WRITE | bt.FLAG_READ,)
	__OTA_DATA_CHAR = (bt.UUID("3E400003-B5A3-F393-E0A9-E50E24DCCA9E"), bt.FLAG_WRITE | bt.FLAG_NOTIFY,)
	
	SERVICE = (
		UUID,
		(
			__OTA_FLAG_CHAR,
			__OTA_DATA_CHAR,
		),
	)

	class Values(object):
		OTA_FLAG_INT = PACK("<B", int(1))

"""蓝牙控制器"""
class BleController:
  def __init__(self, name="glasses"):
    print('init ble controller')
    self.__ble = bt.BLE()
    self.__rx_cb = self.rx_callback
    self.__conn_handle = None
    self.__ota = None

    self.__write = self.__ble.gatts_write
    self.__read = self.__ble.gatts_read
    self.__notify = self.__ble.gatts_notify

    self.__ble.active(False)
    print("activating ble...")
    self.__ble.active(True)
    print("ble activated")

    self.__ble.config(rxbuf=100)
    self.__ble.irq(self.__irq)
    self.__services = (GenericAccess.SERVICE, UartService.SERVICE, OtaService.SERVICE)
    self.__register_services()
    self.__ble.gatts_set_buffer(self.__ota_data_handler, 512)

    self.__adv_payload = BLETools.advertising_generic_payload(
    	services=(UartService.UUID,),
    	appearance=BLEConst.Appearance.GENERIC_EYE_GLASSES,
    )
    self.__resp_payload = BLETools.advertising_resp_payload(
    	name=name,
    	services=[GenericAccess.UUID]
    )

    self.__advertise()

  def __register_services(self):
    (
    	(
        self.__device_name_handle,
        self.__appearance_handle,
        self.__peripheral_preferred_connection_parameters_handle,
        self.__central_address_resolution_handle,
    	),
    	(
        self.__tx_handle,
        self.__rx_handle,
    	),
      (
        self.__ota_flag_handler,
        self.__ota_data_handler,
      ),
    ) = self.__ble.gatts_register_services(self.__services)
    self.__setup_generic_access()
    self.__setup_uart()

  def __setup_generic_access(self):
    self.__write(self.__device_name_handle, GenericAccess.Values.DEVICE_NAME)
    self.__write(self.__appearance_handle, GenericAccess.Values.APPEARANCE)
    self.__write(self.__peripheral_preferred_connection_parameters_handle, GenericAccess.Values.PERIPHERAL_PREFERRED_CONNECTION_PARAMETERS)
    self.__write(self.__central_address_resolution_handle, GenericAccess.Values.CENTRAL_ADDRESS_RESOLUTION)

  def __setup_uart(self):
    self.__write(self.__tx_handle, UartService.Values.TX_VALUE)
    self.__write(self.__rx_handle, UartService.Values.RX_VALUE)

  def __advertise(self, interval_us=500000):
    self.__ble.gap_advertise(None)
    self.__ble.gap_advertise(interval_us, adv_data=self.__adv_payload, resp_data=self.__resp_payload)
    print("advertising...")

  def __irq(self, event, data):
    if event == BLEConst.IRQ.IRQ_CENTRAL_CONNECT:
      self.__conn_handle, addr_type, addr, = data
      print("[{}] connected, handle: {}".format(BLETools.decode_mac(addr), self.__conn_handle))

      self.__ble.gap_advertise(None)
    elif event == BLEConst.IRQ.IRQ_CENTRAL_DISCONNECT:
      self.__conn_handle, _, addr, = data
      print("[{}] disconnected, handle: {}".format(BLETools.decode_mac(addr), self.__conn_handle))

      self.__conn_handle = None
      self.__advertise()
    elif event == BLEConst.IRQ.IRQ_GATTS_WRITE:
      conn_handle, value_handle = data

      if conn_handle == self.__conn_handle and value_handle == self.__rx_handle:
        if self.__rx_cb:
          self.__rx_cb(self.__read(self.__rx_handle).decode().strip())
      if conn_handle == self.__conn_handle and value_handle == self.__ota_flag_handler:
        self.ota_flag_callback(self.__read(self.__ota_flag_handler))
      if conn_handle == self.__conn_handle and value_handle == self.__ota_data_handler:
        self.ota_data_callback(self.__read(self.__ota_data_handler))

  def send(self, data):
    """
    将数据写入本地缓存，并推送到中心设备
    """
    self.__write(self.__tx_handle, data)
    if self.__conn_handle is not None:
      self.__notify(self.__conn_handle, self.__tx_handle, data)

  def ota_notify(self, data):
    self.__notify(self.__conn_handle, self.__ota_data_handler, data)

  def rx_callback(self, data):
    self.__feature_controller.choose_mode(data)
  
  def feature_flag_callback(self, data):
    self.__feature_controller.choose(data)
  
  def ota_flag_callback(self, data):
    self.__ota.end()
    self.__ota = None
  
  def ota_data_callback(self, data):
    if self.__ota is None:
      self.__ota = ota_controller.OTA()
    self.__ota.handle(data)
    self.ota_notify('ok')