---
title: Nginx useful commands
date: 2017-05-29 12:15:20
categories: [DevOps, Nginx]
tags: [Nginx]
image: /assets/img/posts/nginx.png
---
Nginx (pronounced "engine-x") is a free and open-source web server, reverse proxy, load balancer, mail proxy, and HTTP cache. It is known for its high performance, stability, and scalability. Nginx is used by many large websites.
Certainly! Below is a Markdown-formatted guide for configuring Nginx for an Odoo deployment:

# Nginx Configuration for Odoo

Nginx is a popular web server and reverse proxy that can be used to efficiently serve Odoo applications. This guide will walk you through the steps to set up Nginx for your Odoo deployment.

## Prerequisites

Before you begin, ensure you have the following:

- A server running Ubuntu 20.04 or a compatible Linux distribution.
- Odoo installed and configured on your server.
- A domain name pointing to your server's IP address.

## Step 1: Install Nginx

If Nginx is not already installed, you can install it using the following command:

```bash
sudo apt update
sudo apt install nginx
```

## Step 2: Create a Nginx Server Block

In Nginx, a server block is used to define how a particular domain or subdomain should be served. Create a new server block configuration file for your Odoo instance:

```bash
sudo nano /etc/nginx/sites-available/odoo
```

Add the following configuration, adjusting it to match your Odoo setup:

```nginx
server {
    listen 80;
    server_name your_domain.com;

    access_log /var/log/nginx/odoo.access.log;

    location / {
        proxy_pass http://127.0.0.1:8069;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /web/static/ {
        alias /path/to/odoo/static/directory;
    }

    location /longpolling {
        proxy_pass http://127.0.0.1:8072;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    gzip_types text/css text/less text/plain text/xml application/xml application/json application/javascript;
    gzip on;
}
```

Save the file and exit the text editor.

## Step 3: Enable the Nginx Server Block

Enable the Odoo server block by creating a symbolic link in the `sites-enabled` directory:

```bash
sudo ln -s /etc/nginx/sites-available/odoo /etc/nginx/sites-enabled/
```

## Step 4: Test Nginx Configuration

Before you restart Nginx, it's a good practice to test the configuration:

```bash
sudo nginx -t
```

If the test is successful, you should see a message indicating that the configuration is valid.

## Step 5: Restart Nginx

Restart Nginx to apply the changes:

```bash
sudo systemctl restart nginx
```

## Step 6: Update DNS Settings

Update your DNS settings to point your domain name to your server's IP address.

## Step 7: Access Odoo via Nginx

Now you should be able to access your Odoo instance via Nginx using your domain name (e.g., http://your_domain.com). Nginx will act as a reverse proxy and serve your Odoo application.

That's it! You have successfully configured Nginx for your Odoo deployment. Remember to keep your Nginx and Odoo configurations updated and secure to ensure the smooth operation of your application.
## Nginx configurations Examples
```sh
sudo apt-get install nginx
sudo wget -O /etc/nginx/sites-available/tac.com  https://raw.githubusercontent.com/Elbagoury/elbagoury.github.io/main/assets/conf/nginx_https.conf
sudo ln -s /etc/nginx/sites-available/tac.com /etc/nginx/sites-enabled/tac.com
```
