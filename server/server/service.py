# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Yu Huang
# @Email: yuhuang-cst@foxmail.com

import os

# 限制多进程
# os.environ["MKL_NUM_THREADS"] = "1"
# os.environ["NUMEXPR_NUM_THREADS"] = "1"
# os.environ["OMP_NUM_THREADS"] = "1"
# os.environ["KMP_AFFINITY"] = "disabled"

# 禁用GPU
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

from loguru import logger
from sanic import Sanic, response

from server.utils import process_base, print_request, randstr
from server.service_config import ServiceConfig
from server.constant import LOG_PATH
from api import annotate_text

logger.add(os.path.join(LOG_PATH, 'service.log'), retention='10 days')
logger.info('begining-------')

app = Sanic("PhenoBERT")
app.config.update_config(ServiceConfig)

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION'),'r') as fin:
    VERSION = fin.read().strip()


def process_link_res_list(res_list):
    ret_dict = {'result': res_list, 'version': VERSION, 'log_id': randstr(8)}
    return ret_dict


def process_phenobert_input_single_request_inner(request):
    """
    Args:
        request:
            - request.json: {
                'text': str,
            }
    Returns:
        dict: {
            'result': [{
                'span': (int, int),
                'mention_text': str,
                'hpo_code': str,
                'score': float,
                'polarity': str, # 'negative' | 'positive'
            }, ...],
            'version': str,
            'log_id': str,
        }
    """
    # print_request(request) # debug
    text = request.json['text']
    res_list = annotate_text(text)
    res = process_link_res_list(res_list)
    return res


@app.route('/phenobert-input-single', methods=['POST'])
async def process_phenobert_input_single_request(request):
    return process_base(request, process_phenobert_input_single_request_inner)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8085, workers=1, single_process=True)

