#!/usr/bin/env bash
# install nginx and configure it to serve some content
if ! which nginx > /dev/null 2>&1; then
sudo apt-get -y update
sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
myc="\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/\;\n\t}\n"
st="server {"
sudo sed -i "s/^$st/$st$myc/" /etc/nginx/sites-enabled/default
sudo service nginx start
