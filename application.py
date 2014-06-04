from flask import Flask
from flask import render_template
from flask import request
from models import Analise, Numerologia

from dynamodb_mapper.model import ConnectionBorg

application = Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output.
#Make sure to remove this line before deploying to production.
application.debug=True

@application.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        analise = Numerologia.analisar(nome)
        analise.resultado = analise.resultado.decode('unicode-escape')
        analise.save()
        return render_template('index.html', analise = analise)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    try:
        print "Criando tabela..."
        conn = ConnectionBorg()
        conn.set_region("sa-east-1")
        conn.create_table(Analise, 1, 1, wait_for_active=True)
        print "Tabela criada!"
    except:
        print "Erro durante criacao de tabela!"
        pass
    application.run(host='0.0.0.0', debug=True)
