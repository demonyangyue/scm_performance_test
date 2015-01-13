#!/usr/bin/python
#-*- coding=utf-8 -*-

import os
import datetime
import threading

def time_it(func):
    def do(*nkwarg, **kwargs):
        """docstring for do"""
        start_time= datetime.datetime.now()
        func(*nkwarg, **kwargs)
        end_time = datetime.datetime.now()
        return end_time - start_time 
    return do

def multiple_threading(func):
    threads= []
    base_path = os.path.abspath('.')
    def do():
        """docstring for do"""
    for i in [1, 2]:
        thread = threading.Thread(target = func, args=(os.path.join(base_path, str(i)), i))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return do


@time_it
@multiple_threading
def test_sys_cmd(path = '' ,i = 0 ):
    """docstring for test_ls"""
    os.chdir( path)

    os.system("git commit -m '%d'" %(i))
    print "path is %s and i is %d" %(path, i)
    os.system("git push -u origin %d" %(i))


if __name__ == '__main__':
    print test_sys_cmd()
