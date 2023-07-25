# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Yu Huang
# @Email: yuhuang-cst@foxmail.com

import os
import requests
import json
import base64

ip_port = 'http://127.0.0.1:8085'

def test_post_base(url_postfix, req_list):
    print(f'Test: {url_postfix} =======================')
    url = f'{ip_port}/{url_postfix}'
    for i, req in enumerate(req_list):
        r = requests.post(url, data=json.dumps(req))
        tmp = r.json()
        for key in tmp:
            if key.endswith("_post"):
                tmp[key] = str(base64.b64decode(tmp[key]), "utf-8")
        print(f'req = {req}')
        print(f'res = {tmp}')


def test_get_base(url_postfix, req_list):
    print(f'Test: {url_postfix} =======================')
    url = f'{ip_port}/{url_postfix}'
    for i, req in enumerate(req_list):
        r = requests.get(url, params=req)
        print(r.json())


def phenobert_input_single_reqs():
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'test_data', 'phenobert_input_single.json')
    return json.load(open(data_path))


def test_phenobert_input_single():
    test_post_base('phenobert-input-single', phenobert_input_single_reqs())


if __name__ == "__main__":
    test_phenobert_input_single()

