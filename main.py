from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form method = "post">
            <label for = "rot">Rotate by:</label>
            <input id = "rot" type = "text" value = "0" name = "rot"  /> 
            #default value has to be value of zero and not placeholder of "0" since this is an integer.
            <br>
            <br>
            <textarea id = "text" name = "text"> </textarea>
            <br>
            <input type = "submit" />
    
    </body>
</html>
"""

@app.route("/")
def index():
    return form
    
@app.route("/", methods = ['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    #the rotation is an integer in the caesar.py code
    encrypt_message =  request.form['text']
    #we are converting text
    msg_encrypted = rotate_string(encrypt_message, rotation)
    return '<h1>' + msg_encrypted + '<h1>'

app.run()