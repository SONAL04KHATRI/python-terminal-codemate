# 🐍 Python Command Terminal  

A **Python-based terminal emulator** that mimics the behavior of a real system shell.  
Built for the **CodeMate Hackathon**, this project brings together **file operations**, **directory navigation**, and **system monitoring** — all inside a custom Python REPL.  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python">
  <img src="https://img.shields.io/badge/psutil-5.9%2B-green">
  <img src="https://img.shields.io/badge/status-active-brightgreen">
  <img src="https://img.shields.io/github/stars/YOUR-USERNAME/python-terminal?style=social">
</p>

---

## ✨ Features

✅ Fully functional **command terminal** built in Python  
✅ Supports **file & directory operations**: `ls`, `cd`, `pwd`, `mkdir`, `rm`  
✅ Built-in **system monitoring**: `cpu`, `mem`, `ps`  
✅ **Error handling** for invalid commands  
✅ Clean **sandboxed workspace** to prevent unsafe access  
✅ Ready for **extension** — add your own commands!  

---

## 🚀 Quick Start

### 1️⃣ Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/python-terminal.git
cd python-terminal
2️⃣ Setup virtual environment
bash
Copy code
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the terminal
bash
Copy code
python main.py
🖥️ Demo
Here’s a quick look at what the terminal can do:

bash
Copy code
/> ls
# (empty at start)

/> mkdir demo
/> ls
demo/

/> cd demo
/> pwd
/demo

/> cpu
CPU usage: 12.5%
User: 5.0%, System: 3.0%, Idle: 92.0%

/> mem
Total: 15.92GB
Available: 8.21GB
Used: 7.71GB (48%)

/> ps 5
   PID   CPU%   MEM% USER NAME
  1234    5.0    1.2 user python.exe
  5678    2.3    0.8 user code.exe

/> cd ..
/> rm demo
/> ls
# (empty again)

/> exit
Exiting terminal...
🎥 Watch the full demo video here

📂 Project Structure
arduino
Copy code
python-terminal/
│
├── commands/       # all supported commands
│   ├── base.py     # base Command class
│   ├── ls.py       # list files
│   ├── cd.py       # change directory
│   ├── pwd.py      # print working directory
│   ├── mkdir.py    # make directory
│   ├── rm.py       # remove files/dirs
│   ├── cpu.py      # show CPU usage
│   ├── mem.py      # show memory usage
│   └── ps.py       # show processes
│
├── utils/          # helper functions (path resolution, size formatting)
├── tests/          # pytest test cases
├── workspace/      # sandbox root (safe play area)
├── main.py         # entry point
├── terminal.py     # REPL loop
├── requirements.txt
└── README.md
🔮 Optional Enhancements
AI-driven terminal (natural language → commands)

Command history + autocomplete

Web-based terminal UI

🔮 Optional Enhancements
- AI-driven terminal (natural language → commands)
- Command history + autocomplete
- Web-based terminal UI

🤝 Contributing  
Pull requests are welcome!  
If you have an idea for a new command, create a file in `commands/` and extend the `Command` base class.  

⭐ Support  
If you like this project:  
- ⭐ Star this repo on GitHub  
- 🍴 Fork it and build your own commands  
- 🔗 Share it with your friends!  

<p align="center">Made with ❤️ during the CodeMate Hackathon</p>


