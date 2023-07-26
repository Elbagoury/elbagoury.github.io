---
title: Nginx useful commands
date: 2017-05-29 12:15:20
categories: [Nginx, DevOps, Odoo]
tags: [Nginx, DevOps, Odoo]
---
## Nginx configuration
```sh
sudo apt-get install nginx
sudo wget -O /etc/nginx/sites-available/tac.com  https://raw.githubusercontent.com/Elbagoury/DevOps/main/conf/nginx_https.conf
sudo ln -s /etc/nginx/sites-available/tac.com /etc/nginx/sites-enabled/tac.com
```