#!/usr/bin/env bash
# Creating server configuration.
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the required folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a mock HTML file
echo "Hello, I'm NGINX!!!" >> /data/web_statict/releases/test/index.html

# Create a Symbolic Link
sudo ln -sf /data/web_statict/releases/test/ /data/web_statict/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data

# Update the NGINX config to serve the content
sudo sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default

# Restart the NGINX server
sudo service nginx restart

# Exit
exit 0
