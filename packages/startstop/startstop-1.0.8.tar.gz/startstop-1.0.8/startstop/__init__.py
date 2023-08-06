from pyinstrument import Profiler
from time import perf_counter


class StartStopProfiler:
    def __init__(self):
        self.running = False

    def __call__(self, interval=0.001, async_mode="enabled"):
        if not self.running:
            self.profiler = Profiler(interval, async_mode)
            self.profiler.start()
            self.running = True
        else:
            self.profiler.stop()
            self.running = False
            self.profiler.open_in_browser()
            self.profiler.reset()


p = StartStopProfiler()


class StartStopProfilerContext:
    def __init__(self, interval=0.001, async_mode="enabled"):
        self.profiler = Profiler(interval, async_mode)

    def __enter__(self):
        self.profiler.start()

    def __exit__(self, type, value, traceback):
        self.profiler.stop()
        self.profiler.open_in_browser()
        self.profiler.reset()


pc = StartStopProfilerContext


class StartStopTimer:
    def __init__(self):
        self.running = False

    def __call__(self, label: str = "", precision: int = 3):
        if not self.running:
            self.start = perf_counter()
            self.running = True
            self.label = label
            self.precision = precision
        else:
            self.end = perf_counter()
            self.running = False

            if self.label:
                text = f" {self.label}"
            else:
                text = ""

            print(f"TIMER{text}: {self.end - self.start :.{self.precision}f} sec")

            return round(self.end - self.start, precision)


t = StartStopTimer()


class StartStopTimerContext:
    def __init__(self, label: str = "", precision: int = 3):
        self.label = label
        self.precision = precision

    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, type, value, traceback):
        self.end = perf_counter()

        if self.label:
            text = f" {self.label}"
        else:
            text = ""

        print(f"TIMER{text}: {self.end - self.start :.{self.precision}f} sec")


tc = StartStopTimerContext
