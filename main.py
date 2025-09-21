from terminal import Terminal
from pathlib import Path

def main():
    # use a dedicated sandbox folder
    sandbox = Path("workspace")
    sandbox.mkdir(exist_ok=True)   # create if not exists
    term = Terminal(root=sandbox)
    term.run()

if __name__ == "__main__":
    main()
