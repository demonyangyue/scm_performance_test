#!/usr/bin/python
#-*- coding=utf-8 -*-

import os
import datetime
import threading

def time_it(func):
    def do(*nkwarg, **kwargs):
        start_time= datetime.datetime.now()
        func(*nkwarg, **kwargs)
        end_time = datetime.datetime.now()
        return end_time - start_time 
return do

def multiple_threading(func):
    threads= []
    base_path = os.path.abspath('.')
    def do(command):
        """docstring for do"""
        for i in range(20):
            thread = threading.Thread(target = func, args=(command, os.path.join(base_path, str(i))))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
    return do


@time_it
@multiple_threading
def test_sys_cmd(command, path ):
    """docstring for test_ls"""
    os.chdir( path)
    os.system(command)


if __name__ == '__main__':
    print test_sys_cmd("git pull origin master")
