import sys

class ExitProgram:
    def __init__(self, comm):
        self.comms = comm
        
    def exit(self):
        self.comms.kill_elec_ops()
        sys.exit()
