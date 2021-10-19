# Employee Data Web Application
## Author
Nicholas Ngetich
*****
### Description
This is a Django web application with a MySQL database backend for managing employee data.
#### Employee List
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1634657960/screencapture-nick-employee-data-app-herokuapp-employees-2021-10-19-18_31_04_yojpsf.png)
#### Uploads
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1634657959/screencapture-nick-employee-data-app-herokuapp-uploads-2021-10-19-18_31_49_er99zb.png)
*****
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
$ git clone https://github.com/ngetichnicholas/Employee-Data-App.git
```
This will clone the repositoty into your local folder
*****
## Running the cloned App
The first thing to do is to change directory to project folder:
```sh
$ cd Employee-Data-App
```
Open the app with any code editor of your choice to setup environment variables:

To open with VS Code, just run command `$ code .`

### Environment Variables
Create `.env` file and add the following variables and update accordingly
```python
SECRET_KEY='Your-Secret-key'
DEBUG=True
DB_NAME='database-name'
DB_USER='system-user-name'
DB_PASSWORD='database-password'
DB_HOST='127.0.0.1'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
EMAIL_HOST_USER='your-email-address'
EMAIL_HOST_PASSWORD='your-email-password'
CLOUD_API_KEY='your-cloudinary-api-key'
API_SECRET='your-cloudinary-api-secret'
CLOUD_NAME='your-cloudinary-name'
SECURE=True
```

### Virtual Environment
Create a virtual environment to install dependencies and activate it:

```sh
$ python3 -m venv virtual
$ source virtual/bin/activate
```

Then install the dependencies:

```sh
(virtual)$ pip install -r requirements.txt
```
Note the `(virtual)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(virtual)$ python3 manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.
*****
## Dependencies
* django-bootstrap
* Pillow
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
Or you can access the web application directly via this link [https://nick-employee-data-app.herokuapp.com/](https://nick-employee-data-app.herokuapp.com/)
*****
### License
This project is under:  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)
*****
### Questions?
Twitter: **[@ngetichnichoh](https://twitter.com/ngetichnichoh)**  
Email: **[ngetichnicholas903@gmail.com](mailto:ngetichnicholas903@gmail.com)**
