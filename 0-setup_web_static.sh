#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo "Holberton school" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "59i\ \tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default
sudo nginx -t
sudo service nginx restart
