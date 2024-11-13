from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'  # Altere este caminho para onde os arquivos serão armazenados
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Gera um nome de arquivo único usando uuid
            filename = ''.join([uuid.uuid4().hex for _ in range(4)]) + os.path.splitext(file.filename)[1]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))            
            # Gera o link para download
            download_link = url_for('download_file', filename=filename, _external=True)

            # Exibe o link de download na tela
            return f"File uploaded successfully. <br> Download link: <a href='{download_link}'>{download_link}</a>"
    
    # Renderiza o template HTML com CSS incluído
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Upload new File</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #1a1a2e;
                color: #e94560;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }

            .container {
                text-align: center;
            }

            h1 {
                margin-bottom: 50px;
                font-size: 36px;
                text-shadow: 0 0 10px #0f3460, 0 0 20px #0f3460;
            }

            form {
                background: #16213e;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 20px #0f3460, 0 0 30px #0f3460;
            }

            .file-upload-wrapper {
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 20px;
                width: 100%;
            }

            #file-upload {
                display: none;
            }

            .custom-file-upload {
                background-color: #6a0dad;
                color: white;
                padding: 10px 20px;
                border: 2px solid #6a0dad;
                border-radius: 5px;
                cursor: pointer;
                margin-right: 10px;
                font-size: 16px;
                white-space: nowrap;
            }

            .file-name {
                background-color: black;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 16px;
                width: 100%;
                text-align: center;
                border: 1px solid #e94560;
            }

            input[type="submit"] {
                background-color: #e94560;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
            }

            input[type="submit"]:hover {
                background-color: #0f3460;
                color: #e94560;
                box-shadow: 0 0 10px #e94560, 0 0 20px #e94560;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Upload new File</h1>
            <form method="post" enctype="multipart/form-data">
              <div class="file-upload-wrapper">
                  <label for="file-upload" class="custom-file-upload">
                      Browse
                  </label>
                  <div id="file-name" class="file-name">No file selected</div>
                  <input type="file" name="file" id="file-upload" onchange="document.getElementById('file-name').innerText = this.files[0].name">
              </div>
              <input type="submit" value="Upload">
            </form>
        </div>
    </body>
    </html>
    ''')

@app.route('/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)