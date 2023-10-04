#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

if ! service nginx status > /dev/null 2>&1; then
    sudo apt update
    sudo apt install nginx -y

sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"

body_content="Web site under construction!"
current_date=$(date +"%Y-%m-%d %H:%M:%S")
html_content="<html>
  <head></head>
  <body>$body_content</body>
  <p>Generated on: $current_date</p>
</html>"

echo "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo service nginx restart


