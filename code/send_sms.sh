#!/usr/bin/env bash

source ./config.sh

python send_sms.py --phone "$phone" --notification "$notification"
