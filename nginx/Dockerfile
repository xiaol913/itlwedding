FROM nginx:latest

COPY server.crt /etc/nginx/
COPY server.key /etc/nginx/
COPY itl_nginx.conf /etc/nginx/conf.d/
COPY sentry_nginx.conf /etc/nginx/conf.d/
RUN sed -i '/user/{s/nginx/root/}' /etc/nginx/nginx.conf
