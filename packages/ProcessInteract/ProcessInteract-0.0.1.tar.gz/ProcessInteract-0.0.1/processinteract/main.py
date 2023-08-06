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
        self.process.kill()

def exec(*args, shell=False):
    cmd = []
    for arg in args:
        cmd.append(arg)
    subprocess.Popen(cmd, shell=shell)

exec("echo", "hello world")