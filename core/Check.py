# -*- coding: utf-8 -*-

# @author MaliciouSSymbol
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import os
import sys
import platform
import time
from Banner import Printer
from writer import OpenFile
import writer


class Check_req:
    """Checking The Requirments to run the app."""

    def __init__(self):
        self.printer = Printer()

    def check_py_version(self):
        '''checking if the python version valid.
           python3 is not supported at the main script.
           but it requires when running the attacking script.
           you must have both'''

        req_version = '2.7.14'
        not_valid_version = '3.0.0'
        if platform.python_version() >= req_version:
            pass
        elif platform.python_version() >= not_valid_version:
            print(writer.red("python {} is not supported yet\nTry the latest version of python2".format(
                platform.python_version())))
            print('Exiting...')
            time.sleep(2)
            sys.exit(1)

    def SoftwaresExists(self):
        '''Check if the user installed all the required packages.

           Python: Required to run the main script.
           python3: Required to run the model script (Attacking Script).
           unrar: Required to check the password of the archive
           p7zip: Required to check the password of the archive, works as unrar

           [Information]p7zip and unrar is created to create archives and unpack it
           with the extension of zip, 7z and rar.'''

        self.softwares = ['/usr/bin/unrar', '/usr/bin/unzip', '/usr/bin/7z']
        for missing in self.softwares:
            if not os.path.isfile(missing):
                print("Missing file {0}".format(missing))
                sys.exit(1)

    def check_os(self):
        '''Checking if the os is not linux.
           if not linux, do not run :)'''

        req_os = 'posix'
        if os.name != req_os:
            print(writer.red("{} {} is not supported yet".format(
                platform.system(), platform.release())))
            print('Exiting...')
            time.sleep(2)
            sys.exit(1)

    def check_user(self):
        with open('core/configuration/options.conf', 'r') as config:
            lg = config.read()[-5:].strip().__str__()
        if lg == 'user':
            self.login_user()
        elif lg == 'root':
            self.login_root()

    def login_root(self):
        if os.geteuid() != 0:
            print(writer.yellow("Script must run as root!"))
            time.sleep(0.6)
            sys.exit(0)

    def login_user(self):
        if os.geteuid() == 0:
            print(writer.yellow("Script must run as user!"))
            time.sleep(0.6)
            sys.exit(0)
