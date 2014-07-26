# coding=UTF-8

from flask import Flask
from flask import render_template
from flask import request
from models import Analise, Numerologia
from dynamodb_mapper.model import ConnectionBorg
from flask.ext.cdn import CDN
from flask.ext.compress import Compress

try:
    conn = ConnectionBorg()
    conn.set_region("sa-east-1")
    conn.create_table(Analise, 5, 5, wait_for_active=True)
except:
    pass

application = Flask(__name__)

application.debug = False

application.config['CDN_DOMAIN'] = 'cdn.numerologia.ws'
application.config['CDN_TIMESTAMP'] = False
CDN(application)

Compress(application)


@application.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        analise = Numerologia.analisar(nome)
        analise.resultado = analise.resultado.decode('utf-8')
        analise.save()
        return render_template('index.html', analise=analise)
    else:
        return render_template('index.html')


@application.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    application.run(host='0.0.0.0')
