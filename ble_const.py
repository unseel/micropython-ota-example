from micropython import const

class BLEConst(object):
	class ADType(object):
		'''
		Advertising Data Type
		'''
		AD_TYPE_FLAGS = const(0x01) # Flags for discoverability.
		AD_TYPE_16BIT_SERVICE_UUID_MORE_AVAILABLE = const(0x02) # Partial list of 16 bit service UUIDs.
		AD_TYPE_16BIT_SERVICE_UUID_COMPLETE = const(0x03) # Complete list of 16 bit service UUIDs.
		AD_TYPE_32BIT_SERVICE_UUID_MORE_AVAILABLE = const(0x04) # Partial list of 32 bit service UUIDs.
		AD_TYPE_32BIT_SERVICE_UUID_COMPLETE = const(0x05) # Complete list of 32 bit service UUIDs.
		AD_TYPE_128BIT_SERVICE_UUID_MORE_AVAILABLE = const(0x06) # Partial list of 128 bit service UUIDs.
		AD_TYPE_128BIT_SERVICE_UUID_COMPLETE = const(0x07) # Complete list of 128 bit service UUIDs.
		AD_TYPE_SHORT_LOCAL_NAME = const(0x08) # Short local device name.
		AD_TYPE_COMPLETE_LOCAL_NAME = const(0x09) # Complete local device name.
		AD_TYPE_TX_POWER_LEVEL = const(0x0A) # Transmit power level.
		AD_TYPE_CLASS_OF_DEVICE = const(0x0D) # Class of device.
		AD_TYPE_SIMPLE_PAIRING_HASH_C = const(0x0E) # Simple Pairing Hash C.
		AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R = const(0x0F) # Simple Pairing Randomizer R.
		AD_TYPE_SECURITY_MANAGER_TK_VALUE = const(0x10) # Security Manager TK Value.
		AD_TYPE_SECURITY_MANAGER_OOB_FLAGS = const(0x11) # Security Manager Out Of Band Flags.
		AD_TYPE_SLAVE_CONNECTION_INTERVAL_RANGE = const(0x12) # Slave Connection Interval Range.
		AD_TYPE_SOLICITED_SERVICE_UUIDS_16BIT = const(0x14) # List of 16-bit Service Solicitation UUIDs.
		AD_TYPE_SOLICITED_SERVICE_UUIDS_128BIT = const(0x15) # List of 128-bit Service Solicitation UUIDs.
		AD_TYPE_SERVICE_DATA = const(0x16) # Service Data - 16-bit UUID.
		AD_TYPE_PUBLIC_TARGET_ADDRESS = const(0x17) # Public Target Address.
		AD_TYPE_RANDOM_TARGET_ADDRESS = const(0x18) # Random Target Address.
		AD_TYPE_APPEARANCE = const(0x19) # Appearance.
		AD_TYPE_ADVERTISING_INTERVAL = const(0x1A) # Advertising Interval. 
		AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS = const(0x1B) # LE Bluetooth Device Address.
		AD_TYPE_LE_ROLE = const(0x1C) # LE Role.
		AD_TYPE_SIMPLE_PAIRING_HASH_C256 = const(0x1D) # Simple Pairing Hash C-256.
		AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R256 = const(0x1E) # Simple Pairing Randomizer R-256.
		AD_TYPE_SERVICE_DATA_32BIT_UUID = const(0x20) # Service Data - 32-bit UUID.
		AD_TYPE_SERVICE_DATA_128BIT_UUID = const(0x21) # Service Data - 128-bit UUID.
		AD_TYPE_3D_INFORMATION_DATA = const(0x3D) # 3D Information Data.
		AD_TYPE_MANUFACTURER_SPECIFIC_DATA = const(0xFF) # Manufacturer Specific Data.


	class IRQ(object):
		IRQ_CENTRAL_CONNECT = const(1)
		IRQ_CENTRAL_DISCONNECT = const(2)
		IRQ_GATTS_WRITE = const(3)
		IRQ_GATTS_READ_REQUEST = const(4)
		IRQ_SCAN_RESULT = const(5)
		IRQ_SCAN_DONE = const(6)
		IRQ_PERIPHERAL_CONNECT = const(7)
		IRQ_PERIPHERAL_DISCONNECT = const(8)
		IRQ_GATTC_SERVICE_RESULT = const(9)
		IRQ_GATTC_SERVICE_DONE = const(10)
		IRQ_GATTC_CHARACTERISTIC_RESULT = const(11)
		IRQ_GATTC_CHARACTERISTIC_DONE = const(12)
		IRQ_GATTC_DESCRIPTOR_RESULT = const(13)
		IRQ_GATTC_DESCRIPTOR_DONE = const(14)
		IRQ_GATTC_READ_RESULT = const(15)
		IRQ_GATTC_READ_DONE = const(16)
		IRQ_GATTC_WRITE_DONE = const(17)
		IRQ_GATTC_NOTIFY = const(18)
		IRQ_GATTC_INDICATE = const(19)
		IRQ_GATTS_INDICATE_DONE = const(20)
		IRQ_MTU_EXCHANGED = const(21)
		IRQ_L2CAP_ACCEPT = const(22)
		IRQ_L2CAP_CONNECT = const(23)
		IRQ_L2CAP_DISCONNECT = const(24)
		IRQ_L2CAP_RECV = const(25)
		IRQ_L2CAP_SEND_READY = const(26)
		IRQ_CONNECTION_UPDATE = const(27)
		IRQ_ENCRYPTION_UPDATE = const(28)
		IRQ_GET_SECRET = const(29)
		IRQ_SET_SECRET = const(30)

	class Appearance(object):
		Unknown = const(0) # None
		GENERIC_PHONE = const(64) # Generic category
		GENERIC_COMPUTER = const(128) # Generic category
		GENERIC_WATCH = const(192) # Generic category
		WATCH_SPORTS_WATCH = const(193) # Watch subtype
		GENERIC_CLOCK = const(256) # Generic category
		GENERIC_DISPLAY = const(320) # Generic category
		GENERIC_REMOTE_CONTROL = const(384) # Generic category
		GENERIC_EYE_GLASSES = const(448) # Generic category
		GENERIC_TAG = const(512) # Generic category
		GENERIC_KEYRING = const(576) # Generic category
		GENERIC_MEDIA_PLAYER = const(640) # Generic category
		GENERIC_BARCODE_SCANNER = const(704) # Generic category
		GENERIC_THERMOMETER = const(768) # Generic category
		THERMOMETER_EAR = const(769) # Thermometer subtype
		GENERIC_HEART_RATE_SENSOR = const(832) # Generic category
		HEART_RATE_SENSOR_HEART_RATE_BELT = const(833) # Heart Rate Sensor subtype

		# Added Blood pressure support on December 09, 2011
		GENERIC_BLOOD_PRESSURE = const(896) # Generic category
		BLOOD_PRESSURE_ARM = const(897) # Blood Pressure subtype
		BLOOD_PRESSURE_WRIST = const(898) # Blood Pressure subtype

		# Added HID Related appearance values on January 03, 2012 approved by BARB 
		HUMAN_INTERFACE_DEVICE_HID = const(960) # HID Generic
		KEYBOARD = const(961) # HID subtype
		MOUSE = const(962) # HID subtype
		JOYSTICK = const(963) # HID subtype
		GAMEPAD = const(964) # HID subtype
		DIGITIZER_TABLET = const(965) # HID subtype
		CARD_READER = const(966) # HID subtype
		DIGITAL_PEN = const(967) # HID subtype
		BARCODE_SCANNER = const(968) # HID subtype

		# Added Generic Glucose Meter value on May 10, 2012 approved by BARB 
		GENERIC_GLUCOSE_METER = const(1024) # Generic category

		# Added additional appearance values on June 26th, 2012 approved by BARB 
		GENERIC_RUNNING_WALKING_SENSOR = const(1088) # Generic category
		RUNNING_WALKING_SENSOR_IN_SHOE = const(1089) # Running Walking Sensor subtype
		RUNNING_WALKING_SENSOR_ON_SHOE = const(1090) # Running Walking Sensor subtype
		RUNNING_WALKING_SENSOR_ON_HIP = const(1091) # Running Walking Sensor subtype
		GENERIC_CYCLING = const(1152) # Generic category
		CYCLING_CYCLING_COMPUTER = const(1153) # Cycling subtype
		CYCLING_SPEED_SENSOR = const(1154) # Cycling subtype
		CYCLING_CADENCE_SENSOR = const(1155) # Cycling subtype
		CYCLING_POWER_SENSOR = const(1156) # Cycling subtype
		CYCLING_SPEED_AND_CADENCE_SENSOR = const(1157) # Cycling subtype

		# Added appearance values for Pulse Oximeter on July 30th, 2013 approved by BARB 
		GENERIC_PULSE_OXIMETER = const(3136) # Pulse Oximeter Generic Category
		FINGERTIP = const(3137) # Pulse Oximeter subtype
		WRIST_WORN = const(3138) # Pulse Oximeter subtype

		# Added appearance values for Generic Weight Scale on May 21, 2014 approved by BARB 
		GENERIC_WEIGHT_SCALE = const(3200) # Weight Scale Generic Category

		# Added additional appearance values on October 2nd, 2016 approved by BARB 
		GENERIC_PERSONAL_MOBILITY_DEVICE = const(3264) # Personal Mobility Device
		POWERED_WHEELCHAIR = const(3265) # Personal Mobility Device
		MOBILITY_SCOOTER = const(3266) # Personal Mobility Device
		GENERIC_CONTINUOUS_GLUCOSE_MONITOR = const(3328) # Continuous Glucose Monitor

		# Added additional appearance values on February 1st, 2018 approved by BARB 
		GENERIC_INSULIN_PUMP = const(3392) # Insulin Pump
		INSULIN_PUMP_DURABLE_PUMP = const(3393) # Insulin Pump
		INSULIN_PUMP_PATCH_PUMP = const(3396) # Insulin Pump
		INSULIN_PEN = const(3400) # Insulin Pump
		GENERIC_MEDICATION_DELIVERY = const(3456) # Medication Delivery

		# Added appearance values for L&N on July 30th, 2013 approved by BARB 
		GENERIC_OUTDOOR_SPORTS_ACTIVITY = const(5184) # Outdoor Sports Activity Generic Category
		LOCATION_DISPLAY_DEVICE = const(5185) # Outdoor Sports Activity subtype
		LOCATION_AND_NAVIGATION_DISPLAY_DEVICE = const(5186) # Outdoor Sports Activity subtype
		LOCATION_POD = const(5187) # Outdoor Sports Activity subtype
		LOCATION_AND_NAVIGATION_POD = const(5188) # Outdoor Sports Activity subtype

