from subprocess import Popen, PIPE
from os import system, kill, environ
from modules._module import Module
from utils.custom_print import print_ok, print_info, print_error
from utils.check_root import is_root
from utils.dirtytooth.dirtytooth import start_dirtytooth
from utildata.dataset_options import Option


class HomeModule(Module):

    def __init__(self):
        information = {"Name": "Launch Bluetooth Service",
                       "Description": "Launch a bluetooth service",
                       "Author": "@josueencinar",
                       "privileges": "root",}

        # -----------name-----default_value--description--required?
        options = {"bmac": Option.create(name="bmac", required=True),
                   "path": Option.create(name="path", value="/tmp/dirtytooth", required=True, description='Path to save contacts')
                   }

        # Constructor of the parent class
        super(HomeModule, self).__init__(information, options)

    # This module must be always implemented, it is called by the run option
    def run(self):
        if not is_root():
            return
        print_info("Launching Service")
        res = start_dirtytooth(self.args["bmac"], self.args["path"])
        if res == 1:
            print_ok("Done")
        elif res == 0:
            print_error('Process dirtyagent doesn´t exist (use module launch-service first)')
        