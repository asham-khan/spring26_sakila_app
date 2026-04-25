# Name: Muhammad Asham Khan
# Date: 2026-04-25
# Description: Updated DB host and added timeout setting

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))

