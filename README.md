# Python-introduction
* python is all about readability. so 4 x whitespaces are the standard.

## Python Installation
* it's already installed to check the version type: python3 --version
* or: python --version
* to find out which python to use type(in the terminal, this will output '/usr/bin/python3'): which python3
* to install pip (It's like npm) type in terminal: sudo apt-get install python3-pip

### terminal inline coding
* to run a python file in the terminall type: python fileName.py
* to test some code in the terminal type: python3
* to exit type: ctrl+D
* python doesn't really use {} to show end of functions it uses blank spaces. spacing is super inportant.
* a for loop looks like this:
* for i in range(5):
* (4 x spacebar)     x = i * 10
* (4 x spacebar)     print(x)
* an extra empty line shows that the function / code block is complete
* need help on a module? type: help(module_name)
* to exit help type: Q

### Import modules in terminal
* import modules: import module_name
* it import specific function from a module: from module_name import function_name
* example: from math inport factoral
* to rename a function during import: from math import factorial as fac
* to import multiple functions from a module: from module_name import (function_name,function_name2)
* to import everything from a module: from words import *

### Making exportable modules/scripts from functions:
* if __name__ == '__main__': fetch_words()

## advanced command line arguments parsing go to:
* python Standard Library: argparse
* of docopt
* checkout sys.argv[1]

## docstrings
* use """words words words""" in your code.
* this lets you add help file comments in the commandline
* in REPL import the module and then type: help(module_name)
* this will show all the usefull information on all the functions. Pretty cool

## to execute in terminal
* in your file make sure you've got "#! /usr/bin/env python3" on the top of your file
* write in the terminal: chmod +x fileName.py
* and then write in the terminal: ./fileName.py inputHere
* and that will also run the file in the terminal

## Using pip flask to create a web server
* Tutorial: https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
* go to the flask website: http://flask.pocoo.org/docs/0.12/installation/
* I don't think you actually need the virtualenv
* type in terminal: sudo apt-get install python-virtualenv
* once in the project folder run: virtualenv venv
* now when your working on a specif project you just type in terminal: . venv/bin/activate
* if you want to exit the virtual envirnoment just type: deactivate
* Install Flask: sudo pip install Flask

## Installing MySQL
* website: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04
* First update the defualt package byt typing in the terminal : sudo apt-get update
* Then install mySQL by typing in the terminal: sudo apt-get install mysql-server
* To set the security on mysql type in the terminal: sudo mysql_secure_installation
* note: you might need to initialise the database (it will abort if you didn't need to) type in terminal: mysqld --initialize
* To test the MySQL is working, type in terminal: systemctl status mysql.service
* If it didn't start on it's own, type in terminal (I used the commmand above): sudo /etc/init.d/mysql start
* you can also test it by connecting to the db by using the admin tool(-u = root and -p = password): mysqladmin -p -u root version
* to stop MySQL, type in terminal(I just hit ctrl+c in the terminal):  sudo /etc/init.d/mysql stop
* to uninstall MySQL: sudo apt-get purge mysql*
* then: sudo apt-get autoremove
* then: sudo apt-get autoclean

## Easy to use interface for MySQL:
* You can use MySQL Workbench: https://www.mysql.com/products/workbench/
* note: it can migrate other databases to mysql. It's also works with cloud and other exciting things.
* Another one is HeidiSQL:  https://www.heidisql.com/
* Another is phpMyAdmin: https://www.phpmyadmin.net/
* and another lightweight one is adminer: https://www.adminer.org/
* there is also one on ubuntu called mysql-query-browser: https://apps.ubuntu.com/cat/applications/natty/mysql-query-browser/
* adminer didn't work and heidi works with ubuntu wine (microsoft)

## to use Workbench
* in the terminal type: sudo apt-get update
* then: sudo apt-get install mysql-workbench
* then go to ubuntu installer and search for workbench click install.
* to uninstall: sudo apt-get remove mysql-workbench
* then: sudo apt-get purge mysql-workbench

## Using MySQL
* to make database: sudo mysql -u root -p
* to get help file type in terminal: 'help;' or '\h' for help. Type '\c' to clear current input statement
* to quit type: \q
* to create a database type in terminal(it shoud show mysql> I've called the database BucketList): CREATE DATABASE <databaseName>;
* to specify which database to use type in terminal: USE BucketList;
* CREATE TABLE `BucketList`.`tbl_user` (
  `user_id` BIGINT UNIQUE AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_username` VARCHAR(45) NULL,
  `user_password` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));

* to Query the table write (this will show nothing for now): SELECT * FROM tbl_user;

* Now create a stored procedure called 'sp_createUser', type in the terminal:
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN

        select 'Username Exists !!';

    ELSE

        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );

    END IF;
END$$
DELIMITER ;
