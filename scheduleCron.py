# crontab -e should look like this to load the env vars...
# SHELL=/bin/bash
# */5 * * * * source /home/austintackaberry/.bash_profile; python2 /home/austintackaberry/github/goes-notify/goes-notify.py --config /home/austintackaberry/github/goes-notify/config.json



from crontab import CronTab

my_cron = CronTab(user='austintackaberry')

job = my_cron.new(command='python2 /home/austintackaberry/github/goes-notify/goes-notify.py --config /home/austintackaberry/github/goes-notify/config.json')

job.minute.every(1)

my_cron.write()