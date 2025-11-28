import sys

class PythonVersion:

    @staticmethod
    def get_version_info():
        return sys.version

print(PythonVersion.get_version_info())