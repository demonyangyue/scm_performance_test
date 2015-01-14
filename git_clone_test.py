#!/usr/bin/python
#-*- coding=utf-8 -*-

import os
from config import REMOTE_REPOSITORY
from utils import *


@calculate_time
@multiple_threading
def git_clone(thread_index = -1):
    os.system("git clone %s %d" %(REMOTE_REPOSITORY, thread_index))

if __name__ == '__main__':
    total_time = git_clone()
    print total_time
