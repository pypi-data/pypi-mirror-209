from setuptools import setup, find_packages
from setuptools.extension import Extension
from setuptools.dist import Distribution
from setuptools.command.build_ext import build_ext
import os

class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

class BuildBinary(build_ext):
    def run(self):
        build_ext.run(self)
        self.copy_extensions_to_bin()

    def copy_extensions_to_bin(self):
        for ext in self.extensions:
            build_lib = os.path.abspath(self.build_lib)
            dest = os.path.join(build_lib, os.path.dirname(ext.name))
            src = self.get_ext_fullpath(ext.name)
            if not os.path.exists(dest):
                os.makedirs(dest)
            self.copy_file(src, dest)

setup(
    name='robot_package',
    version='1.0.3',
    description='Controlling the Jaco2 robot',
    packages=find_packages(),
    cmdclass={'build_ext': BuildBinary},
    include_package_data=True,
    distclass=BinaryDistribution,
    package_data={'': ['bin/jaco2.pyd', 'bin/jaco2.dll', 'bin/CommandLayerEthernet.dll', 'bin/CommandLayerWindows.dll', 'bin/CommunicationLayerEthernet.dll',  'bin/CommunicationLayerWindows.dll']},
)




