FROM centos
MAINTAINER Shawn Gao <xxlangdou@gmail.com>
ENV TZ "Asia/Shanghai"

# Install python3.7.0 and required libs
WORKDIR /tmp
COPY ./requirements.txt ./
ADD ./Python-3.6.5.tgz ./
RUN yum upgrade -y && \
    yum groupinstall "Development tools" -y && \
    yum install -y zlib-devel bzip2-devel openssl-devel \
    ncurses-devel sqlite-devel readline-devel tk-devel \
    libffi-devel vim python-devel mysql-devel && \
    ./Python-3.6.5/configure --prefix=/usr/local && \
    make && make altinstall && \
    rm -rf ./Python-3.6* && \
    # Edit default env
    rm -rf /usr/bin/python && \
    ln -s /usr/local/bin/python3.6 /usr/bin/python && \
    ln -s /usr/local/bin/pip3.6 /usr/bin/pip && \
    sed -i '/\#\!\/usr\/bin/{s/python/python2/}' /usr/bin/yum && \
    sed -i '/\#\! \/usr\/bin/{s/python/python2/}' /usr/libexec/urlgrabber-ext-down && \
    # Upgrade pip
    pip install --upgrade pip -i https://pypi.douban.com/simpe && \
    # Install requirement lib
    pip install -i https://pypi.douban.com/simple -r /tmp/requirements.txt && \
    # Clean caches
    yum clean headers packages metadata
 
STOPSIGNAL SIGTERM
