#!/usr/bin/python
#-*- coding=utf-8 -*-

import os
from utils import *
from config import BASE_DIR


@calculate_time
@multiple_threading
def git_pull(thread_index = -1):
    repository_path = generate_local_repository_path(thread_index)
    os.system("git -C %s pull origin master" %(repository_path))


if __name__ == '__main__':
    #first we change something in one repository and push to remote
    sample_thread_index = 0
    repository_path = generate_local_repository_path(sample_thread_index)
    os.system("git -C %s pull origin master" %(repository_path))
    modify_repository_content(sample_thread_index)
    push_change_to_remote(sample_thread_index, "master")

    #then we go to each local repository and pull from remote
    total_time = git_pull()
    print total_time
