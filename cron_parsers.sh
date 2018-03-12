#! /bin/bash

source /home/ubuntu/newsdiffs_env/bin/activate
cd /home/ubuntu/newsdiffs
python website/manage.py scraper > /home/ubuntu/newsdiffs/logs/$(date +'%Y-%m-%d-%H-%M').log 2>&1 &
