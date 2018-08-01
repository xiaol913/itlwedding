# 个站展示页面
Quick Start
-----
(Need Python-3.6.5.tgz)

1.    Move files
      
      /bin/bash sh -C build.sh

2.    Build sentry images

      cd ../sentry && docker-compose build

4.    Generate a secret key. Add it to docker-compose.yml in base as SENTRY_SECRET_KEY

      docker-compose run --rm web config generate-secret-key

5.    Migrate data

      docker-compose run --rm web upgrade

6.    Start sentry server

      docker-compose up -d

7.    Start web server

      cd .. && docker-compose up -d
