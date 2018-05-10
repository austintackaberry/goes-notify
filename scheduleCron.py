from crontab import CronTab

my_cron = CronTab(user='austintackaberry')

job = my_cron.new(command='python2 /home/austintackaberry/github/goes-notify/goes-notify.py --config /home/austintackaberry/github/goes-notify/config.json')

job.minute.every(5)

my_cron.write()