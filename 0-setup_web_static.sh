#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

trap 'exit 0' ERR

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx -y
fi
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"

body_content="Holberton School Web site under construction!"
current_date=$(date +"%Y-%m-%d %H:%M:%S")
html_content="<html>
  <head></head>
  <body>$body_content</body>
  <p>Generated on: $current_date</p>
</html>"

echo "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo wget -q -O /etc/nginx/sites-available/default http://exampleconfig.com/static/raw/nginx/ubuntu20.04/etc/nginx/sites-available/default
config="/etc/nginx/sites-available/default"
echo 'Holberton School Hello World!' | sudo tee /var/www/html/index.html > /dev/null
sudo sed -i '/^}$/i \ \n\tlocation \/redirect_me {return 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;}' $config
sudo sed -i '/^}$/i \ \n\tlocation @404 {return 404 "Ceci n'\''est pas une page\\n";}' $config
sudo sed -i 's/=404/@404/g' $config
sudo sed -i "/^server {/a \ \tadd_header X-Served-By $HOSTNAME;" $config
sudo sed -i '/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $config

sudo service nginx restart
