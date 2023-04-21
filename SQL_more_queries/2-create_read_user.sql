-- Script that creates the database hbtn_0d_2 and the user user_0d_2.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'hbtn_0c_0' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'hbtn_0c_0';
