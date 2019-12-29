# crontab -e should look like this:

# SHELL=/bin/bash
# * * * * * source /home/austintackaberry/.bash_profile; python2 /home/austintackaberry/dev/goes-notify/goes-notify.py --config /home/austintackaberry/dev/goes-notify/config.json

from crontab import CronTab

my_cron = CronTab(user='austintackaberry')

job = my_cron.new(command='python2 /home/austintackaberry/dev/goes-notify/goes-notify.py --config /home/austintackaberry/dev/goes-notify/config.json')

job.minute.every(1)

my_cron.write()