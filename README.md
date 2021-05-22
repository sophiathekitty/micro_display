# Micro Display

a micro display using a raspberry pi zero and mini PiTFT hat. testing out pulling this to the pi so maybe i can have them do automatic pulls...

all in one package for hardware: <https://www.adafruit.com/product/4475>

## Setup

first run the raspberry pi config wizard and get everything setup so you can ssh into the pi and it's connected to your network

```bash
sudo raspi-config
```

### All in One super command to install everything

this is what i've used to setup a few raspberry pi zeros... slightly modified to install some different python libraries... it's kinda terrifying to run. here's hoping i didn't mess up the pi... lol well it seems to have crashed this time. i'll see if i can finish the setup and use the command log to update this setup.

```bash
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install apache2 -y && sudo a2enmod rewrite && sudo service apache2 restart && sudo apt-get install php -y && sudo apt-get install libapache2-mod-php -y && sudo apt-get install mariadb-server -y && sudo apt-get install php-mysql -y && sudo service apache2 restart && sudo apt-get install python -y && sudo apt-get install python-serial -y && sudo apt-get install python-serial -y && sudo ln -s /var/www/html www && sudo chown -R pi:pi /var/www/html && sudo chmod 777 /var/www/html && sudo apt-get install git -y && sudo apt-get install python-urllib3 -y
```

### Individual commands

for when you wanna take your time and not sit around worried about what's happening

```bash
sudo apt-get update
```

```bash
sudo apt-get upgrade -y
```

```bash
sudo apt-get install apache2 -y
```

```bash
sudo a2enmod rewrite
```

```bash
sudo service apache2 restart
```

```bash
sudo apt-get install php -y
```

```bash
sudo apt-get install libapache2-mod-php -y
```

```bash
sudo apt-get install mariadb-server -y
```

```bash
sudo apt-get install php-mysql -y
```

```bash
sudo service apache2 restart
```

```bash
sudo apt-get install python -y
```

```bash
sudo apt-get install python-serial -y
```

```bash
sudo apt-get install python-pip -y
```

```bash
sudo ln -s /var/www/html www
```

```bash
sudo chown -R pi:pi /var/www/html
```

```bash
sudo chmod 777 /var/www/html
```

```bash
sudo apt-get install git -y
```

```bash
sudo apt-get install python-urllib3 -y
```

### Setup the mysql database

```bash
sudo mysql -u root
```

```mysql
[MariaDB] use mysql;
[MariaDB] update user set plugin='' where User='root';
[MariaDB] flush privileges;
[MariaDB] \q
```

This needs to be followed by the following command:

```bash
mysql_secure_installation
```

```bash
sudo ln -s /var/www/html www && sudo chown -R pi:pi www && sudo chmod 777 www
```

## Tools

favicon generator: <https://www.favicon-generator.org/>
