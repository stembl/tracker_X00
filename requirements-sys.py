# tracker/requriements_sys.py

"""
Installs the system requirements for the tracker project.

Run
---
$ sudo python requirements-sys.py

"""

from subprocess import STDOUT, check_call, CalledProcessError
import os

packages = [
    'python-smbus',
    'python-gps',
    'gpsd',
    'gpsd-clients',
    'libgps-dev'
]

for package in packages:
    try:
        check_call(['apt-get', 'install', '-y', package],
                    stdout=open (os.devnull, 'wb'), stderr=STDOUT)
    except CalledProcessError as e:
        raise RuntimeError(
            "command '{}' return with error (code {}): {}"

            .format(e.cmd, e.returncode, e.output))
