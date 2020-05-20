FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /EShop
WORKDIR /EShop
COPY /EShop/requirements.txt /EShop/
RUN pip install -r requirements.txt
COPY . /EShop/
