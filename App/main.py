import os
from flask import Flask, redirect, render_template, jsonify, request, send_from_directory, flash
from flask_cors import CORS
from sqlalchemy.exc import OperationalError

def create_app():
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'MySecretKey'
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.app_context().push()
    return app

app = create_app()

# migrate = get_migrate(app)

@app.route('/', methods=['GET'])
def homePage():
  return render_template('homePage.html')

@app.route('/signup', methods=['GET'])
def signUp():
  return render_template('signUp.html')

@app.route('/about', methods=['GET'])
def about():
  return render_template('about.html')

@app.route('/faqs', methods=['GET'])
def faqs():
  return render_template('faqs.html')

@app.route('/records', methods=['GET'])
def records():
  return render_template('records.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)