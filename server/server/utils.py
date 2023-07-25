# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Yu Huang
# @Email: yuhuang-cst@foxmail.com

import time
import string
import random
from sanic import response
from loguru import logger
import traceback

def randstr(num):
    return ''.join(random.sample(string.ascii_letters + string.digits, num))


def process_base(request, inner_func):
    try:
        start_time = time.time()
        resp = inner_func(request)
        resp['ret_code'] = 0; resp['ret_message'] = 'succeed'
        resp = response.json(resp, ensure_ascii=False)
        logger.info('Time Cost: {} seconds'.format(time.time() - start_time))
        return resp
    except:
        err_msg = str(traceback.format_exc())
        logger.error(err_msg)
        err = {'ret_code': 1, 'ret_message': err_msg}
        return response.json(err)


def print_request(request):
    """
    Args:
        request (sanic.Request):
    """
    print(f'request = {request}')
    try:
        print(f'request.args = {request.args}') # get method
    except Exception as e:
        print(e)
    try:
        print(f'request.json = {request.json}')
    except Exception as e:
        print(e)
    print(f'request.form = {request.form}')
    print(f'request.body = {request.body}')
    print(f'request.files = {request.files}')



if __name__ == '__main__':
    pass
