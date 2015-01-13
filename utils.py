#!/usr/bin/python
#-*- coding=utf-8 -*-

#define some useful decorators

from config import CONCURRENCY_NUM
import datetime
import threading

def calculate_time(func):
    def wrapped(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        return end_time - start_time
    return wrapped


def multiple_threading(func):
    threads = []
    def wrapped(*arg, **kwargs):
        for thread_index in range(CONCURRENCY_NUM):
            thread = threading.Thread(target = func, args = (thread_index,) )
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
    return wrapped
            
