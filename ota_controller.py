from esp32 import Partition
from micropython import const

BLOCKLEN = const(4096)

class OTA:
  def __init__(self) -> None:
    self.part = Partition(Partition.RUNNING).get_next_update()
    self.block = 0
    self.buf = bytearray(BLOCKLEN)
    self.buf_len = 0
    self.total = 0
  
  def handle(self, msg):
    msglen = len(msg)
    self.total += msglen
    print('receiving msg of length', msglen, self.total)
    if self.buf_len + msglen >= BLOCKLEN:
      # got a full block, assemble it and write to flash
      copy_len = BLOCKLEN - self.buf_len
      self.buf[self.buf_len : BLOCKLEN] = msg[:copy_len]
      self.part.writeblocks(self.block, self.buf)
      self.block += 1
      msglen -= copy_len
      if msglen > 0:
        self.buf[:msglen] = msg[copy_len:]
      self.buf_len = msglen
    else:
      self.buf[self.buf_len : self.buf_len + msglen] = msg
      self.buf_len += msglen
  
  def end(self):
    print('end ota')
    if self.buf_len > 0:
      for i in range(BLOCKLEN - self.buf_len):
        self.buf[self.buf_len + i] = 0xFF  # erased flash is ff
      self.part.writeblocks(self.block, self.buf)
      self.block += 1
    self.finish()
  
  def finish(self):
    del self.buf
    self.part.set_boot()


  

  