FROM python:3

WORKDIR /usr/src/app

ADD bayes_master.py /usr/src/app

ADD file.json /usr/src/app

RUN pip install requests

EXPOSE 5006

CMD [ "python", "./bayes_master.py" ]

