#!/usr/bin/python
#-*- coding=utf-8 -*-

#define some useful decorators

from config import CONCURRENCY_NUM, BASE_DIR
import datetime
import threading
import random
import os

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


def simulate_file_change(file_name):
    #simulate changing file content by shuffling lines, so we will have some delta to pull/push
    with open(file_name, 'r') as input_file:
        lines = input_file.readlines()
    random.shuffle(lines)
    with open(file_name, 'w') as output_file:
        output_file.writelines(lines)

def generate_local_repository_path(thread_index):
    return os.path.join(BASE_DIR, str(thread_index))

def modify_repository_content(thread_index):
    #modify some content in the repository, commit the change
    repository_path = generate_local_repository_path(thread_index)
    simulate_file_change(os.path.join(repository_path, "unzip.pl"))
    os.system("git -C %s commit -a -m %d" %(repository_path, thread_index))

def push_change_to_remote(thread_index , remote_branch):
    #push to a remote branch which uses the thread index as branch name
    repository_path = generate_local_repository_path(thread_index)
    os.system("git -C %s push -u origin master:%s" %(repository_path, remote_branch))

            
