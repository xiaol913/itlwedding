# 个站展示页面
Quick Start
-----
(Need Python-3.6.5.tgz)


/bin/bash sh -C build.sh

cd sentry

docker-compose build

docker-compose run --rm web config generate-secret-key # Generate a secret key. Add it to docker-compose.yml in base as SENTRY_SECRET_KEY

docker-compose run --rm web upgrade

docker-compose up -d

cd ..

docker-compose up -d
