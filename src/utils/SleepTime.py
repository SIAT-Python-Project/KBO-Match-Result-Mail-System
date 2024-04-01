import time
from typing import Callable

class SleepTime:
    def __init__(self, sleep_time: int) -> None:
        self.__sleep_time = sleep_time

    def __call__(self, func: Callable[[None], None]) -> Callable[[None], None]:
        def call_and_sleep(*args, **kwargs):
            value = func(*args, **kwargs)

            time.sleep(self.__sleep_time)

            return value
        
        return call_and_sleep