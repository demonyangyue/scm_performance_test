#!/usr/bin/python
#-*- coding=utf-8 -*-

import os
from utils import *
from config import BASE_DIR


@calculate_time
@multiple_threading
def git_push(thread_index = -1):
    #just use thread index as the new remote branch name
    modify_repository_content(thread_index)
    push_change_to_remote(thread_index, str(thread_index))
    

if __name__ == '__main__':
    total_time = git_push()
    print total_time
