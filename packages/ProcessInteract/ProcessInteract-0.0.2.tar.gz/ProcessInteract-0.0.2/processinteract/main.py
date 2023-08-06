import subprocess
import psutil

class Process():
    def __init__(self, PID=int):
        """
        Initiates a process class with own PID
        """
        self.pid = PID
        self.process = psutil.Process(PID)

    def kill(self):
        """
        Kills the process
        """
        self.process.kill()

def exec(command=None, *args, shell=False):
    """
    Executing command with args in new console window
    """
    cmd = []
    cmd.append(command)
    for arg in args:
        cmd.append(arg)
    subprocess.Popen(cmd, shell=shell)
