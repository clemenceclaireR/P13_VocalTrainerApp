#!/bin/sh

find /home/clemence/site/db_backups -name "*.pgsql" -type f -mtime +7 -exec rm {} \;