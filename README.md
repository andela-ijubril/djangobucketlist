# Django powered bucketlist application

![My Bucketlist](http://3.bp.blogspot.com/-GWeanJf2zR4/UQexkAuMA-I/AAAAAAAAAwg/sKi4y94TCcE/s1600/Bucket-List-e1336246406457.png)

### Description:
We only live once lets make it count by doing so many awesome stuffs. 
 [Awesomebucket](http://awesomebucket.herokuapp.com/) is an application that helps to manage  all the awesome things you want to do in life before kicking the bucket. 
Awesomebucket is powered by the framework for perfecionist with a deadline "Django"


### Technology used
Awesome bucket is built with the following stack:

* [Django](https://www.djangoproject.com/) - Django makes it easier to build better Web apps more quickly and with less code.
* [Djangorestframework](http://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [Twitter Bootstrap](http://getbootstrap.com/) - great UI boilerplate for modern web apps
* [jquery](https://jquery.com/) - The Write Less, Do More, JavaScript Library.
* [django swagger](http://django-rest-swagger.readthedocs.org/en/latest/) - An API documentation generator for Swagger UI and Django REST Framework.

### API Documentation
The Api documentation can be found [here](http://awesomebucket.herokuapp.com/docs)
## Requirements
To install and run this application, you need to have python installed on your machine.
### Installation
To install the build locally 
```
$ git clone https://github.com/andela-ijubril/djangobucketlist.git
$ cd djangoucketlist
$ pip install -r requirements.txt
```
Set Up your environment key
```
$ touch .env.yml
$ echo 'SECRET_KEY="any-key-you-wish"
```
### Run your build
```
$ python bucketlist/manage.py runserver --settings=settings.development
```

### Running the test
To run your test
```
$ python manage.py test
```
### Coverage
```
$ coverage run manage.py test
$ coverage report
```

Contributing
============

This is an open source project. Anxiously waiting to get your feedback in the form of
[`issues`](https://github.com/andela-ijubril/djangobucketlist/issues) and [`pull requests`](https://github.com/andela-ijubril/djangobucketlist/pul) so that we can make the world a better place by giving people an opportunity to have an awesome life