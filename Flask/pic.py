# ADDING THE IMAGE

# IMPORTING
from flask import Flask, render_template
import os

# Interaction
app = Flask(__name__)

picfolder = os.path.join('static')   #Joining the static and pics folder
app.config['UPLOAD_FOLDER'] = picfolder   #Configuring the upload folder

# Mapping
@app.route('/') 

# Inputs
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'download.jpeg')   #Joining the upload folder and the image
    return render_template('home.html', user_image=pic)   #Output on the browser

@app.route('/second')
def second():
    return render_template('second.html')   
 
# MAIN FUNCTION
if __name__ == '__main__':
    app.run(debug=True)