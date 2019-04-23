from robot.api.deco import keyword
from salabsutils import DynamicRobotApiClass,PY2
from robotremoteserver import RobotRemoteServer
import os
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from glob import glob
import base64


class RemoteTransfer(DynamicRobotApiClass):
    @keyword
    def transfer_files(self, pattern = "*.png"):
        items = {}
        results = glob(os.path.join(self.log_directory,pattern))
        items['amount'] = len(results)
        items['log_directory'] = self.log_directory
        items['files'] = []
        for item in results:
            with open(item, "rb") as input_buffer:
                buff = base64.b64encode(input_buffer.read())
                items['files'].append({"name": item, "data": buff})
        return items

    @keyword
    def save_files(self, file_array):
        for item in file_array['files']:
            new_filename = os.path.join(self.log_directory, os.path.basename(item['name']))
            with open(new_filename, 'wb') as output_buffer:
                output_buffer.write(base64.b64decode(item['data']))

    @property
    def log_directory(self):
        try:
            logfile = BuiltIn().get_variable_value("${LOG FILE}")
            if logfile is None:
                return BuiltIn().get_variable_value("${OUTPUTDIR}")
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwdu() if PY2 else os.getcwd()  # pylint: disable=no-member


if __name__ == '__main__':
    RobotRemoteServer(RemoteTransfer())
