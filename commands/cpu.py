import psutil
from .base import Command

class CpuCommand(Command):
    """cpu - show CPU usage"""

    def execute(self, args, terminal):
        try:
            percent = psutil.cpu_percent(interval=0.5)
            times = psutil.cpu_times_percent(interval=None, percpu=False)
            print(f"CPU usage: {percent}%")
            print(f"User: {times.user}%, System: {times.system}%, Idle: {times.idle}%")
        except Exception as e:
            print(f"cpu error: {e}")
