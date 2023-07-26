---
title: Odoo useful commands
date: 2015-03-29 12:15:20
categories: [Odoo, Development]
tags: [DevOps, Odoo, Bash, Linux]
---
Odoo is a popular open-source ERP software that can be customized and integrated with various modules. One of the ways to interact with Odoo is through the terminal, where you can execute various commands to manage your Odoo instance. Some of the useful terminal commands for Odoo are:

- `odoo-bin -c config_file` : This command allows you to start Odoo with a specific configuration file, where you can specify the database name, port, addons path, log level, and other options.
- `odoo-bin -d database_name -i module_name`: This command allows you to install a specific module in a specific database. You can also use -u instead of -i to update an existing module.
- `odoo-bin -d database_name --db-filter=regex`: This command allows you to filter the databases that Odoo will show on the web interface, based on a regular expression. For example, if you have multiple databases with different prefixes, you can use this command to only show the ones that match your prefix.
- `odoo-bin shell -d database_name`: This command allows you to open an interactive Python shell with the Odoo environment loaded. You can use this shell to access the Odoo models, browse records, create or modify data, and run custom scripts.
- `odoo-bin scaffold module_name path` : This command allows you to create a skeleton for a new Odoo module, with the basic files and folders. You can specify the path where you want to create the module, or use the default addons path.

## Monitoring
Check services
```sh
ps aux | grep odoo
sudo service odoo-server status
sudo service postgresql status
sudo /etc/init.d/postgresql status
sudo service postgresql start
```
View logs
```sh
tail -f /odoo/filestore/production/log/odoo-server.log
tail -f /odoo/filestore/staging/log/odoo-server.log
tail -n 1000 /odoo/filestore/production/log/odoo-server.log
```
Find Errors/Warnings
```sh
grep ERROR /odoo/filestore/production/log/odoo-server.log
grep WARNING /odoo/filestore/production/log/odoo-server.log
grep ir_cron /odoo/filestore/production/log/odoo-server.log
```
## Devolopment
Odoo scaffold
```sh
./odoo-bin  scaffold -t  tac  "TAC President Dashboard "  odoo/custom
```
## Configuration
Copy conf file

```sh
sudo wget -O /etc/odoo-server.conf  https://raw.githubusercontent.com/Elbagoury/DevOps/main/conf/odoo.conf
```
