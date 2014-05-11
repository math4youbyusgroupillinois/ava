#!/bin/bash
sudo tail -f /var/log/apache2/error.log /var/log/apache2/access.log /var/log/apache2/other_vhosts_access.log
