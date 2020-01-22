#!/usr/bin/env bash
# install nginx
# shellcheck disable=SC1117
sudo apt-get update -y
sudo apt-get install nginx -y

# create the folders
mkdir -p /data
mkdir -p /data/web_static/releases
mkdir /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# create links
if [ -L /data/web_static/current ]; then
        rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# give ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx Config
sed -i "s=^server {=server {\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}=" /etc/nginx/sites-available/default

# restart
sudo service nginx restart
