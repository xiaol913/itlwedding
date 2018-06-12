# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM python:3.6.5
MAINTAINER Shawn Gao <xxlangdou@gmail.com>
ENV TZ "Asia/Shanghai"
ENV PROJECT_DIR = /itlwedding

RUN mkdir /itlwedding
RUN mkdir /iltwedding/db -p

# Copy the project files
WORKDIR $PROJECT_DIR
ADD . ./

# Install vim
# RUN apt-get update
# RUN apt-get install vim -y

# Install all libraries
RUN pip install -i https://pypi.douban.com/simple -r requirements.txt

# Remove not essential files
RUN find /usr/lib/python2.7 -name '*.pyc' -delete && \
    find /usr/lib/python3 -name '*.pyc' -delete && \
    find /usr/lib/python3.5 -name '*.pyc' -delete && \
    find /usr/local/lib/python2.7 -name '*.pyc' -delete && \
    find /usr/local/lib/python3.5 -name '*.pyc' -delete && \
    rm -rf /root/.cache && apt-get autoclean && \
    rm -rf /tmp/* /var/lib/apt/* /var/cache/* /var/log/*
