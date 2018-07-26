FROM centos
MAINTAINER Shawn Gao <xxlangdou@gmail.com>
ENV TZ "Asia/Shanghai"

WORKDIR /tmp/
ADD ./Python-3.7.0.tar.xz ./
ADD ./requirements.txt ./
RUN yum upgrade -y && \
    yum groupinstall "Development tools" -y && \
    yum install -y zlib-devel bzip2-devel openssl-devel \
    ncurses-devel sqlite-devel readline-devel tk-devel \
    libffi-devel vim python-devel mysql-devel && \
    tar xvJf Python-3.7.0.tar.xz
WORKDIR /tmp/Python-3.7.0
RUN ./configure --prefix=/usr/local && \
    make && make altinstall && \
    rm -rf Python-3.7*
RUN rm -rf /usr/bin/python && \
    ln -s /usr/local/bin/python3.7 /usr/bin/python && \
    ln -s /usr/local/bin/pip3.7 /usr/bin/pip && \
    python -m pip install --upgrade pip && \
    sed -i '/\#\!\/usr\/bin/{s/python/python2/}' /usr/bin/yum && \
    sed -i '/\#\! \/usr\/bin/{s/python/python2/}' /usr/libexec/urlgrabber-ext-down
RUN pip install -i https://pypi.douban.com/simple -r requirements.txt
