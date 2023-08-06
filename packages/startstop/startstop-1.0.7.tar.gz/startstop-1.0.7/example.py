from startstop import p, pc, t, tc


def your_code():
    for i in range(100000):
        i**2


# Simple timer
t()
your_code()
t()


# Simple timer with label and precision config
t(label="your label", precision=2)
your_code()
t()


# Simple timer as contex manager
with tc():
    your_code()


# Simple timer as contex manager label and precision config
with tc(label="your label", precision=2):
    your_code()


# Profiler
p()
your_code()
p()


# Profiler with config
p(interval=0.01, async_mode="enabled")
your_code()
p()


# Profiler as contex manager
with pc():
    your_code()


# Profiler as contex manager with config
with pc(interval=0.002, async_mode="enabled"):
    your_code()
