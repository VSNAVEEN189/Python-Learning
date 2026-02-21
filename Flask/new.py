# IMPORTING THE FLASK MODULE
from django.shortcuts import render
from flask import Flask, render_template, request

# Interactionbetween flask and localhost
app = Flask(__name__)  # Object name

# Mapping
@app.route('/')        #Routed or mapped to the url
@app.route('/register')   #Routed or mapped to the url

# Inputs
def homepage():
    return render_template('register.html')   #Output on the browser

# Mapping
@app.route('/confirmation', methods=['POST','GET'])   #Routed or mapped to the url
def register():
    if request.method == 'POST':        #If the method is post
        n = request.form['name']         #Getting the name from the form
        p = request.form['phone number'] #Getting the phone from the form
        c = request.form['city']         #Getting the city from the form
        return render_template('confirm.html', name=n, city=c, phonenumber=p)   #Output on the browser

# MAIN FUNCTION
if __name__ == '__main__':
    app.run(debug=True)  

