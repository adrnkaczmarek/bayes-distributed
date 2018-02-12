FROM python:3

WORKDIR /usr/src/app

ADD naiveBayesClassifier /usr/src/app/naiveBayesClassifier

ADD ./bayes_worker.py /usr/src/app

RUN pip install flask

EXPOSE 5002

CMD [ "python", "./bayes_worker.py", "5002" ]

