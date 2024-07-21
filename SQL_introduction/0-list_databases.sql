#!/bin/bash

-- This script logs into MySQL and lists all databases

-- Replace 'username' with your MySQL username
USERNAME="root"

-- Prompt for password
echo "root"
read -s PASSWORD

-- Execute the MySQL command to show databases
mysql -u $USERNAME -p$PASSWORD -e "SHOW DATABASES;"


