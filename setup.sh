# sqlite3 ticker_data.db < create_spot_tables.sql

# conda env create -f conda_environment.yml

# Run populate database via cron
# * * * * * zsh -i /Users/mconn/precision_crypto/cronjobs/populate_database.sh >/tmp/stdout.log 2>/tmp/stderr.log

# Stuff for EC2 NGINX
# cat /etc/nginx/conf.d/react.conf 
# cat /lib/systemd/system/react.service 