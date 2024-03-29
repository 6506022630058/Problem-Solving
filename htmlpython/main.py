from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField,TextAreaField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField('File',validators=[InputRequired()])
    submit = SubmitField('Upload File')

class UploadText(FlaskForm):
    text = TextAreaField('Text',validators=[InputRequired()])
    submit = SubmitField('Upload text')

@app.route('/',methods = ['GET','POST'])
@app.route('/home',methods = ['GET','POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "File has been uploaded"
    return render_template('index.html',form = form)

@app.route('/',methods = ['GET','POST2'])
@app.route('/p1',methods = ['GET','POST2'])
def p1():
    form = UploadText()
    if form.validate_on_submit():
        text = form.text.data
        print(text)
    return render_template('index.html',form = form)

if __name__ == "__main__":
    app.run(debug=True)