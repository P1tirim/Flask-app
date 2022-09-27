from flask import request
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/GET')
def Get_Users():
    f = open('file.txt','r')
    users = f.read();
    f.close();
    return users;

@app.route('/api/POST', methods = ['POST', 'GET'])
def Post_User():
    if request.method == 'POST':
        f = open('file.txt','w')
        name = request.form['username']
        password = request.form['password']
        email = request.form['email']
        group = request.form['group']
        iq = request.form['iq']
        f.write(name + " " + password + "" + email + " " + group + " " + iq +"\n")
        f.close()


 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3005')
