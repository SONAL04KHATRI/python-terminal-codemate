import psutil
from utils.helpers import format_size
from .base import Command

class MemCommand(Command):
    """mem - show memory usage"""

    def execute(self, args, terminal):
        try:
            vm = psutil.virtual_memory()
            print(f"Total: {format_size(vm.total)}")
            print(f"Available: {format_size(vm.available)}")
            print(f"Used: {format_size(vm.used)} ({vm.percent}%)")
        except Exception as e:
            print(f"mem error: {e}")
