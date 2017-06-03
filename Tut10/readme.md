# databases
* sqlite comes pre-installed with python3
* postgreSQL aren't pre-installed.
* make a backup: `sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak`
* append the new line: `echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" | sudo tee -a /etc/apt/sources.list`
* to install type: `wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  sudo apt-key add -
sudo apt-get update`
* the outputs are: `Ver Cluster Port Status Owner    Data directory               Log file
9.4 main    5432 down   postgres /var/lib/postgresql/9.4/main /var/log/postgresql/postgresql-9.4-main.log`

* `9.6 main    5433 down   postgres /var/lib/postgresql/9.6/main /var/log/postgresql/postgresql-9.6-main.log
`
* `sudo apt-get update`
* https://help.ubuntu.com/stable/serverguide/postgresql.html
* `pip3 install psycopg2`
* then setup other stuff:
* `sudo -u postgres psql template1` //to create a database called template1
* restart postgres: `sudo systemctl restart postgresql.service`
* `ALTER USER postgres with encrypted password 'your_password';`
* USER = postgres password = postgres
* to use psql type: `sudo -u postgres psql`
* in psql to create a database: `create database name;`
* to switch to database: `\connect databaseName;`
* to view table: `\x`& `\d tableName;`
* \l to show all databases
* \dt to list all tables
* \h for help with SQL commands
* \? for help with psql commands
* \g or terminate with semicolon to execute query
* \q to quit
* remove a database: `drop database if exists name;`
* https://dba.stackexchange.com/questions/1285/how-do-i-list-all-databases-and-tables-using-psql
* `sudo apt install postgresql-client`
* `sudo apt install postgresql-doc-9.1`
