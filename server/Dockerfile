#FROM csighub.tencentyun.com/jarvis_med_sec/tlinux-based-image:tlinux2.2-python3.6
#FROM inveniosoftware/centos8-python:3.7
#FROM loging/centos8-python37:latest
#FROM gfadevel/centos7-python37
#FROM dipcode/centos7-python37:latest
FROM centos:8

LABEL MAINTAINER="yuhuang<yuhuang-cst@foxmail.com>"
ENV VERSION=1.0.1

# change yum source; aliyun repo download: wget https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo
RUN rm -rf /etc/yum.repos.d/*
COPY ./Centos-vault-8.5.2111.repo /etc/yum.repos.d/CentOS-Base.repo
RUN yum clean all && yum makecache

# install python3.7.11
ENV PYTHON_VERSION "3.7.11"
RUN yum install -y wget tar zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel xz-devel
RUN yum install -y gcc
RUN yum install -y make
RUN wget https://npm.taobao.org/mirrors/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
    && tar -zxvf Python-${PYTHON_VERSION}.tgz \
    && cd Python-${PYTHON_VERSION} \
    && ./configure prefix=/usr/local/python3 \
    && make \
    && make install \
    && make clean \
    && rm -rf /Python-${PYTHON_VERSION}*
ENV PATH="/usr/local/python3/bin:${PATH}"

# install pip
RUN yum -y install epel-release python3-pip python3-devel

# set language env
RUN yum -y install glibc-locale-source glibc-langpack-en glibc-langpack-zh
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8

## install gcc7 (fastext need)
#RUN yum -y install centos-release-scl \
#    && yum -y install devtoolset-7-gcc*
#SHELL [ "/usr/bin/scl", "enable", "devtoolset-7"]

## install lzma（stanza need）
#RUN yum install -y xz-devel python-backports-lzma

# create file folder & copy project
RUN mkdir -p /data/PhenoBERT \
    && mkdir -p /data/server
COPY ./PhenoBERT /data/PhenoBERT
COPY ./server /data/server
ENV PYTHONPATH=/data/PhenoBERT/phenobert/utils:/data

# install requirements
COPY ./requirements.txt /data
RUN pip3 install --upgrade pip -i http://mirrors.tencent.com/pypi/simple/ --trusted-host mirrors.tencent.com
RUN pip3 install -r /data/requirements.txt -i http://mirrors.tencent.com/pypi/simple/ --trusted-host mirrors.tencent.com
RUN pip3 install pybind11 -i http://mirrors.tencent.com/pypi/simple/ --trusted-host mirrors.tencent.com
RUN pip3 install -r /data/PhenoBERT/requirements.txt -i http://mirrors.tencent.com/pypi/simple/ --trusted-host mirrors.tencent.com

COPY ./py_pre_download.py /data
RUN python3 /data/py_pre_download.py

WORKDIR /data/PhenoBERT/phenobert/utils

# EXPOSE 50051

ENTRYPOINT ["python3", "../../../server/service.py"]
