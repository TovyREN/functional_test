def test_add(self, a, b):
    assert a + b == self.add(a, b)

def test_subtract(self, a, b):
    assert a - b == self.subtract(a, b)

def test_multiply(self, a, b):
    assert a * b == self.multiply(a, b)

def test_divide(self, a, b):
    assert a / b == self.divide(a, b)

def test_power(self, a, b):
    assert a ** b == self.power(a, b)

def test_sqrt(self, a):
    assert a ** 0.5 == self.sqrt(a)

def test_clear_memory(self):
    self.memory == 0
