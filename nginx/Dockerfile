FROM nginx:latest

WORKDIR /etc/nginx/

COPY ./server.crt ./
COPY ./server.key ./
COPY ./itl_nginx.conf ./conf.d/itl_nginx.conf
COPY ./sentry_nginx.conf ./conf.d/sentry_nginx.conf
RUN rm -rf /etc/nginx/nginx.conf
COPY ./nginx.conf ./
