# config.py
# Author: Abdul Rafay Saad | Date: 2026-04-25
# Description: Added health check interval

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
