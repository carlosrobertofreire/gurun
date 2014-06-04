from flask import Flask
from flask import render_template

application = Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output.
#Make sure to remove this line before deploying to production.
application.debug=True

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
