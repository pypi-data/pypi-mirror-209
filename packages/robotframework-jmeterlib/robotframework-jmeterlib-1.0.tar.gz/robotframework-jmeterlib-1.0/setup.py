#Robot Framework JMeter Library
#

"""
To install Robot Framework JMeter Library execute command:
    python setup.py install
"""
from distutils.core import setup

setup(name='robotframework-jmeterlib',
      version='1.0',
      description='Robot Framework JMeter Library',
      author='Satish',
      author_email='emaseaccela@gmail.com',
      license='none',
      url='https://github.com/kowalpy/Robot-Framework-JMeter-Library',
      py_modules=['JMeterLib', 'JMeterClasses'],
      data_files=[('Scripts', ['jmeterLibExample.txt']),
                  ('Doc', ['JMeterLib.html'])]
      )