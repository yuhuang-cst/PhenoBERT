# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Yu Huang
# @Email: yuhuang-cst@foxmail.com

import os

class ServiceConfig(object):
    # If not set fall back to production for safety
    SANIC_ENV = os.getenv('PHENOBERT', 'production')
    DEBUG = bool(os.getenv('DEBUG', False))

    # Set SANIC_SECRET on your production Environment
    SECRET_KEY = os.getenv('PHENOBERT_SECRET', 'secret')


if __name__ == '__main__':
    pass
