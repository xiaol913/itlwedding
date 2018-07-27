#!/bin/bash

echo '========== Start to building =========='
sleep 2

echo '===== moving files ====='
sleep 2
#mv ./db ../
#mv ./nginx ../
#mv ./sentry ../
#mv ./docker-compose.yml ../

echo '===== creating netword ====='
sleep 2
#docker network create shawnlive
cd ../sentry
#mkdir -p ./data/{sentry,postgres}

echo '===== building sentry images(1) ====='
sleep 2
docker-compose build
key=`docker-compose run --rm web config generate-secret-key | tail -1`

echo "===== the key is $key ====="
sleep 2
sed -i "/SENTRY_SECRET_KEY:/{s/''/'$key'/}" ./docker-compose.yml

echo '===== building sentry images(2) ====='
sleep 2
/bin/expect << -EOF
    set timeout 30
    spawn docker-compose run --rm web upgrade
    expect {
        "*create a user account now*" { send "y\r"; exp_continue }
        "Email*" { send "admin@admin.com\r"; exp_continue } 
        "Password*" { send "123456\r"; exp_continue }
        "Repeat for confirmation*" { send "123456\r"; exp_continue }
        "Should this user be a superuser*" { send "y\r" }
    }
    expect eof
-EOF

echo '===== start sentry ====='
sleep 2
docker-compose up -d

echo '===== building web server images ====='
sleep 2
cd ../
docker-compose build
docker-compose up -d

echo '========== End of building =========='
