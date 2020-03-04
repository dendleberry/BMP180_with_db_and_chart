#! /bin/bash

commands="CREATE DATABASE IF NOT EXISTS sewer;
CREATE USER IF NOT EXISTS 'dbuser'@'%' IDENTIFIED BY 'dbpassword';
GRANT ALL privileges ON sewer.* TO 'dbuser'@'%';
FLUSH PRIVILEGES;
USE sewer;
CREATE OR REPLACE TABLE pressures (id INT PRIMARY KEY AUTO_INCREMENT, timestamp TIMESTAMP, reading VARCHAR(20));
CREATE OR REPLACE TABLE smells (id INT PRIMARY KEY AUTO_INCREMENT, smellTime TIMESTAMP);"

echo "${commands}" | /usr/bin/mysql -u root -p

