# Employee Data Web Application
## Author
Nicholas Ngetich
*****
### Description
This is a Django web application with a MySQL database backend for managing employee data.

### Prerequisites
* Text editor eg Visual Studio Code
* You need to have git installed. You can install it with the following command in your terminal
`$ sudo apt install git-all`
*****
## Cloning the application
To access this project on your local files, you can clone it using these steps
1. Open your terminal
1. Use this command to clone:
```sh
`$ git clone https://github.com/ngetichnicholas/Employee-Data-App.git`
```
 
1. This will clone the repositoty into your local folder
*****
## Running the cloned App
The first thing to do is to change directory to project folder:
```sh
`$ cd Employee-Data-App`
```

Create a virtual environment to install dependencies in and activate it:

```sh
`$ python3 -m venv virtual`
`$ source virtual/bin/activate`
```

Then install the dependencies:

```sh
`(virtual)$ pip install -r requirements.txt`
```
Note the `(virtual)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
`(virtual)$ python3 manage.py runserver`
```
And navigate to `http://127.0.0.1:8000`.

*****
## Dependencies
* django-bootstrap
* Pillow
* cloudinary
* psycopg2
* django-registration
* python-decouple
* Python Venv
* whitenoise
* gunicorn
*****
## Technologies Used
* Python 3
* HTML
* JavaScript
* CSS
******
### Live Link
Or you can access the web application directly via this [LIVE LINK]().
*****
### License
This project is under:  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)
*****
### Questions?
Twitter: **[@ngetichnichoh](https://twitter.com/ngetichnichoh)**  
Email: **[nicholas.ngetich@student.moringaschool.com](mailto:nicholas.ngetich@student.moringaschool.com)**
