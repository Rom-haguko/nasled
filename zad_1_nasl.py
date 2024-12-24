class Counter:
    def __init__(self, start = 0):
        self.value = start

    def inc(self, x=1):
        self.value += x

    def dec(self, x=1):
        self.value -= x
        if self.value < 0:
            self.value = 0

class NonDecCounter(Counter):
    def dec(self, x=1):
        pass

class LimitedCounter(Counter):
    def __init__(self, start = 0, limit = 10):
        super().__init__(start)
        self.limit = limit

    def inc(self, x=1):
        self.value = min(self.limit, self.value + x)

counter = Counter(5)
print("Counter:")
print("Начальное значение:", counter.value)
counter.inc()
print("После inc():", counter.value)
counter.dec(3)
print("После dec(3):", counter.value)
counter.dec(10)
print("После dec(10):", counter.value)

print("\nNonDecCounter:")
non_dec_counter = NonDecCounter(5)
print("Начальное значение:", non_dec_counter.value)
non_dec_counter.inc(10)
print("После inc(10):", non_dec_counter.value)
non_dec_counter.dec(5)
print("После dec(5):", non_dec_counter.value)

print("\nLimitedCounter:")
limited_counter = LimitedCounter(5, 15)
print("Начальное значение:", limited_counter.value)
limited_counter.inc(7)
print("После inc(7):", limited_counter.value)
limited_counter.inc(5)
print("После inc(5):", limited_counter.value)
limited_counter.dec(3)
print("После dec(3):", limited_counter.value)