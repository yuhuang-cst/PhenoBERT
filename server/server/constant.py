# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Yu Huang
# @Email: yuhuang-cst@foxmail.com

import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CODE_PATH = os.path.join(PROJECT_PATH, 'server')
TEST_DATA_PATH = os.path.join(PROJECT_PATH, 'test_data')
LOG_PATH = os.path.join(PROJECT_PATH, 'log'); os.makedirs(LOG_PATH, exist_ok=True)

if __name__ == '__main__':
    print(f'PROJECT_PATH = {PROJECT_PATH}')

