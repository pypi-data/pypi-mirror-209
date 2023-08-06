import os
import sys
from typing import List

from travel.tools.executable import Executable


class Python(Executable):

    def __init__(self, path: str = None, pre_command: str = None):
        path = path or os.environ.get("TRAVEL_PYTHON_PATH", sys.executable)
        self.path = f'"{path}"'
        super().__init__(self.path, pre_command=pre_command)
        # TODO version from Popen

    def replace_process(self, command: List[str]):
        os.execv(self.path, [os.path.basename(os.path.normpath(self.path)), *command])


main_python = Python()
