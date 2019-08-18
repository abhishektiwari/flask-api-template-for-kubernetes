#!/bin/bash

source venv/bin/activate

echo 'I am here'
while true; do
    flask deploy
    flask seed_db
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done


gunicorn -b 0.0.0.0:5000 entry:app
