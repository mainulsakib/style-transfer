from flask import Flask, render_template, request, send_file
import os
from style_transfer import style_transfer
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['OUTPUT_FOLDER'] = 'static/outputs'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        content_file = request.files['content']
        style_file = request.files['style']
        
        if content_file and style_file:
            content_filename = str(uuid.uuid4()) + os.path.splitext(content_file.filename)[1]
            style_filename = str(uuid.uuid4()) + os.path.splitext(style_file.filename)[1]
            
            content_path = os.path.join(app.config['UPLOAD_FOLDER'], content_filename)
            style_path = os.path.join(app.config['UPLOAD_FOLDER'], style_filename)
            
            content_file.save(content_path)
            style_file.save(style_path)
            
            output_filename = str(uuid.uuid4()) + '.png'
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            
            style_transfer(content_path, style_path, output_path)
            
            return render_template('result.html', result=output_filename)
    return render_template('upload.html')



    

@app.route('/output/<filename>')
def output_file(filename):
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], filename), mimetype='image/png')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    app.run(debug=True)