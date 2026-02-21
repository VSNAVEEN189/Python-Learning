# REDIRECTING USING HYPERLINKS IN FLASK

# IMPORTING
from flask import Flask, render_template

# Interaction
app = Flask(__name__)

# Mapping
@app.route('/') 

# Inputs
def first():
    return render_template('home.html')

@app.route('/second')
def second():
    # return "Welcome to the second page"   #First method
    return render_template('second.html')   #Second method
 
# MAIN FUNCTION
if __name__ == '__main__':
    app.run(debug=True)