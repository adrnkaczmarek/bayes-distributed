from flask import Flask, request, jsonify
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier
import logging
import json
import sys


def init_logger():
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logger.setLevel(logging.INFO)
    open('example.log', 'w+')
    handler = logging.FileHandler('example.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


port = int(sys.argv[1])
newsTrainer = Trainer(tokenizer.Tokenizer(stop_words=[], signs_to_remove=["?!#%&"]))
app = Flask(__name__)
log = init_logger()


@app.route('/add', methods=['POST'])
def add():
    #log.info("Request to add data to model")
    data = json.loads(request.data)
    newsTrainer.train(data['Smoking'], data['M..Work']+data['P..Work']+data['Pressure']+data['Proteins']+data['Family'])
    #log.info(request.data)
    return request.data


@app.route('/test', methods=['POST'])
def test():
    log.info("Request to ask model")
    news_classifier = Classifier(newsTrainer.data, tokenizer.Tokenizer(stop_words=[], signs_to_remove=["?!#%&"]))
    data = json.loads(request.data)
    classification = news_classifier.classify(data['wynik'])
    log.info(classification)
    return jsonify(classification)


@app.route('/test1', methods=['GET'])
def test1():
    news_classifier = Classifier(newsTrainer.data, tokenizer.Tokenizer(stop_words=[], signs_to_remove=["?!#%&"]))
    unknown_instance = 'no'
    classification = news_classifier.classify(unknown_instance)
    print(classification)
    return jsonify(classification)


if __name__ == '__main__':
    log.info("Worker started")
    app.run(host='0.0.0.0', port=port)
