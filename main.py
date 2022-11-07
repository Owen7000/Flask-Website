import random
from flask import Flask
from flask import render_template as rt

app = Flask( __name__, template_folder='templates', static_folder='static')

@app.route('/')
def base():
  return rt('base.html', )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))