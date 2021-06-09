import sys
from comms import Communications


class ExitProgram:
    def __init__(self, comm: Communications, app):
        self.comms: Communications = comm
        self.app = app

    def Exit(self):
        self.comms.kill_elec_ops()