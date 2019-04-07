from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    <body>
        <form method = "post">
            <label for = "rot">Rotate by:</label>
            <input id = "rot" type = "text" value = "0" name = "rot"  /> 
            
            <br>
            <br>
            <textarea id = "text" name = "text">{0} </textarea>
            <br>
            <input type = "submit" />
    
    </body>
</html>
"""
#default value has to be value of zero and not placeholder of "0" since this is an integer.
@app.route("/")
def index():
    return form.format("")
    
@app.route("/", methods = ['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    #the rotation is an integer in the caesar.py code
    encrypt_message =  request.form['text']
    #we are converting text
    msg_encrypted = rotate_string(encrypt_message, rotation)
    #return '<h1>' + msg_encrypted + '<h1>'
    return form.format(msg_encrypted)

app.run()