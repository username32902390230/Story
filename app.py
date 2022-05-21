from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello from flaskk'
	
# this is a pointless comment to be able to do a new git add test
