FROM nginx:latest

COPY itl_nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/itl_nginx.conf /etc/nginx/conf.d/
RUN sed -i '/user/{s/nginx/root/}' /etc/nginx/nginx.conf
