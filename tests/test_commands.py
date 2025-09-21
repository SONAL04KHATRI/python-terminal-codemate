"""
Basic pytest tests for the core file/directory commands.
Run with: pytest -q
"""

import os
from pathlib import Path
import shutil
import tempfile
from terminal import Terminal
from commands.ls import LsCommand
from commands.mkdir import MkdirCommand
from commands.cd import CdCommand
from commands.pwd import PwdCommand
from commands.rm import RmCommand

def test_mkdir_cd_ls_rm(tmp_path):
    # Initialize terminal sandboxed to tmp_path
    term = Terminal(root=str(tmp_path))
    # mkdir testdir
    cmd = MkdirCommand()
    cmd.execute(["testdir"], term)
    assert (tmp_path / "testdir").exists()

    # cd testdir
    cd = CdCommand()
    cd.execute(["testdir"], term)
    assert term.cwd == (tmp_path / "testdir").resolve()

    # pwd prints expected (we'll capture using PwdCommand)
    pwd = PwdCommand()
    # just run (shouldn't raise)
    pwd.execute([], term)

    # create file and ls
    (term.cwd / "file1.txt").write_text("hello")
    ls = LsCommand()
    ls.execute([], term)  # should list file1.txt (not asserting print output here)

    # rm file
    rm = RmCommand()
    rm.execute(["file1.txt"], term)
    assert not (term.cwd / "file1.txt").exists()

    # rm non-existent should print error but not raise
    rm.execute(["nonexistent.txt"], term)
