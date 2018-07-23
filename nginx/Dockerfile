FROM nginx:latest

WORKDIR /etc/nginx/
COPY ./server.crt ./
COPY ./server.key ./
COPY ./itl_nginx.conf ./conf.d/itl_nginx.conf
COPY ./sentry_nginx.conf ./conf.d/sentry_nginx.conf
RUN sed -i '/user/{s/nginx/root/}' /etc/nginx/nginx.conf
