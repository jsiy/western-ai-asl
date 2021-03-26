import os

from flask import request, redirect
from flask import Flask
from flask import render_template
from werkzeug.utils import secure_filename
from getPrediction import get_prediction


app = Flask(__name__)
app.config['UPLOADS'] = './static/'

@app.route('/', methods=["GET", "POST"])



def upload_file():
    if request.method == 'POST':

        if request.files:

            image = request.files["image"]
        
        print("Classifying image...")
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOADS'], filename))
        print(filename)
        prediction = get_prediction(filename)
        print(prediction)
        return render_template('output.html', prediction=prediction) 

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
