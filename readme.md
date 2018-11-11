# Choco task

**An complete Django application template, with Django, Celery, RabbitMQ**

<!-- Use this Flask app to initiate your project with less work. In this application  template you will find the following plugins already configured: -->


## Requirements

Python 3.5+, python-pip, virtualenv

## Instalation

First, clone this repository:

    $ git clone https://github.com/turkpenbayev/choco-task.git
    $ cd choco

Install Pip on linux:

    $ sudo apt-get install python-pip

**Installing Redis**
Redis is a complete, stable, and durable message broker that can be used with Celery. Installing Redis on Ubuntu based systems is done through the following command:

    $ apt-get install -y erlang
    $ sudo apt-get install redis-server

Then start the Redis service:

    $ systemctl start redis-server
    $ systemctl status redis-server

**Starting The Worker Process**
Open a new terminal tab, and run the following command:

    $ celery -A choco worker -l info

To install virtualenv globally with pip (if you have pip 1.3 or greater installed globally):

    $ sudo pip install virtualenv


After, install all necessary to run:

    $ pip install -r requirements.txt

Than, run the application:

	$ python manage.py runserver 0.0.0.0:8000

To see your application, access this url in your browser: 

	http://0.0.0.0:8000

All configuration is in: `printf/settings.py`
