FROM centos
MAINTAINER Shawn Gao <xxlangdou@gmail.com>
ENV TZ "Asia/Shanghai"

RUN yum upgrade -y && \
    yum -y install make zlib zlib-devel gcc-c++ libtool  openssl openssl-devel wget
WORKDIR /tmp/
RUN wget http://nginx.org/download/nginx-1.7.4.tar.gz && \
    tar -zxvf nginx-1.7.4.tar.gz
WORKDIR /tmp/nginx-1.7.4
RUN ./configure --prefix=/usr/local/nginx && make && make install &&
\
    rm -rf nginx*

WORKDIR /usr/local/nginx/
COPY ./itl_nginx.conf ./conf.d/itl_nginx.conf
COPY ./sentry_nginx.conf ./conf.d/sentry_nginx.conf
RUN rm -rf ./nginx.conf
COPY ./nginx.conf ./
