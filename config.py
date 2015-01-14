#!/usr/bin/python
#-*- coding=utf-8 -*-
import os

REMOTE_REPOSITORY = "git@10.27.19.133:automation/buildscripts.git"
CONCURRENCY_NUM = 3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#for debug
if __name__ == '__main__':
    print BASE_DIR
