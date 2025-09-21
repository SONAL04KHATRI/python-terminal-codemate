import psutil
from operator import itemgetter
from .base import Command

class PsCommand(Command):
    """ps [n] - show top n processes by CPU"""

    def execute(self, args, terminal):
        try:
            n = int(args[0]) if args else 10
            processes = []
            for p in psutil.process_iter(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
                info = p.info
                processes.append({
                    'pid': info.get('pid'),
                    'name': info.get('name') or '',
                    'user': info.get('username') or '',
                    'cpu': info.get('cpu_percent') or 0.0,
                    'mem': info.get('memory_percent') or 0.0,
                })
            procs_sorted = sorted(processes, key=itemgetter('cpu'), reverse=True)[:n]
            print(f"{'PID':>6} {'CPU%':>6} {'MEM%':>6} USER NAME")
            for p in procs_sorted:
                print(f"{p['pid']:>6} {p['cpu']:6.1f} {p['mem']:6.1f} {p['user']} {p['name']}")
        except Exception as e:
            print(f"ps error: {e}")
