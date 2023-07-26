---
title: Nginx useful commands
date: 2017-05-29 12:15:20
categories: [DevOps, Nginx]
tags: [Nginx]
image:
  path: assets/img/posts/nginx.png
---
Nginx (pronounced "engine-x") is a free and open-source web server, reverse proxy, load balancer, mail proxy, and HTTP cache. It is known for its high performance, stability, and scalability. Nginx is used by many large websites.

## Nginx configuration
```sh
sudo apt-get install nginx
sudo wget -O /etc/nginx/sites-available/tac.com  https://raw.githubusercontent.com/Elbagoury/DevOps/main/conf/nginx_https.conf
sudo ln -s /etc/nginx/sites-available/tac.com /etc/nginx/sites-enabled/tac.com
```