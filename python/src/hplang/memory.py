class Buffer:

  def __init__(self):
    self.mem = [0]
    self.pos = 0

  @property
  def cur(self) -> int:
    return self.mem[self.pos]

  def dec(self):
    self.mem[self.pos] = (self.mem[self.pos] - 1) % 256

  def inc(self):
    self.mem[self.pos] = (self.mem[self.pos] + 1) % 256

  def next(self):
    if self.pos == len(self.mem) - 1:
      self.mem.append(0)
      self.pos += 1
    else:
      self.pos += 1

  def prev(self):
    self.pos -= 1
