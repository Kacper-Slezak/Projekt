from flask import render_template, request, redirect, flash, url_for
from app import app, csrf
from app.forms import UploadForm
import os
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Plik został przesłany!', 'success')
            return redirect(url_for('upload_file'))
        else:
            flash('Niepoprawny format pliku!', 'danger')
    return render_template('main.html', form=form)
