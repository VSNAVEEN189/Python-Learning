# Importing
from flask import Flask, render_template

# Interaction
app = Flask(__name__)

# Mapping
@app.route('/')     

# Inputs
def first():
    return render_template('index.html')   #Output on the browser

# MAIN FUNCTION
if __name__ == '__main__':
    app.run(debug=True)