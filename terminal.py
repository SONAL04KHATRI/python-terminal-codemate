import shlex
from pathlib import Path
from commands import registry
from utils.helpers import safe_resolve

class Terminal:
    def __init__(self, root: str = None):
        # Sandbox root = current folder if not specified
        self.root = Path(root).resolve() if root else Path.cwd().resolve()
        self.cwd = self.root
        self.env = {}

    def prompt_path(self):
        try:
            rel = self.cwd.relative_to(self.root)
            return f"/{rel}" if str(rel) != "." else "/"
        except Exception:
            return str(self.cwd)

    def resolve_path(self, target: str) -> Path:
        return safe_resolve(self.root, self.cwd, target)

    def run(self):
        print(f"Python Command Terminal — sandbox root: {self.root}")
        while True:
            try:
                raw = input(f"{self.prompt_path()}> ").strip()
                if not raw:
                    continue
                if raw in ("exit", "quit"):
                    print("Exiting terminal...")
                    break

                parts = shlex.split(raw)
                cmd_name = parts[0]
                args = parts[1:]

                if cmd_name in registry:
                    CommandClass = registry[cmd_name]
                    cmd = CommandClass()
                    try:
                        cmd.execute(args, self)
                    except Exception as e:
                        print(f"{cmd_name} error: {e}")
                else:
                    print(f"Unknown command: {cmd_name} — try one of {', '.join(registry.keys())}")

            except KeyboardInterrupt:
                print("\nUse 'exit' or 'quit' to leave the terminal.")
            except EOFError:
                print("\nEOF received. Exiting.")
                break
            except Exception as e:
                print(f"REPL error: {e}")
