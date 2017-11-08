# -*- coding: utf-8 -*-
import os
import platform

class Check_req:
    """Checking The Requirments to run the app."""
    def check_py_version(self):
        '''checking if the python version valid'''
        req_version = '2.7.14'
        not_valid_version = '3.0.0'
        if platform.python_version()>=req_version:
            pass
        elif platform.python_version()>=not_valid_version:
            print("python %s is not supported yet\nTry the latest version of python2" % platform.python_version())
            print('Exiting...')
            time.sleep(2)
            sys.exit(1)

    def check_os(self):
        '''Checking if the os is not linux'''
        req_os = 'posix'
        if os.name!=req_os:
            print("%s %s is not supported yet" % (platform.system(), platform.release()))
            print('Exiting...')
            time.sleep(2)
            sys.exit(1)
