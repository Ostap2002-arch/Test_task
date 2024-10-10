FROM python:3.12.5

RUN mkdir /market

WORKDIR /market

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh