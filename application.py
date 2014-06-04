from flask import Flask
from flask import render_template
from flask import request
from models import Analise, Numerologia

application = Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output.
#Make sure to remove this line before deploying to production.
application.debug=True

@application.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        analise = Numerologia.analisar(nome)
        print "Nome %s analisado com sucesso! Soma %d - Resultado %s" % (analise.nome, analise.valor, analise.resultado)
        return render_template('index.html', analise = analise)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
