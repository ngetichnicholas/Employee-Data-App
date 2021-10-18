FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /employee_data_app
WORKDIR /employee_data_app
ADD requirements.txt /employee_data_app/
RUN pip install -r requirements.txt
ADD . /employee_data_app/