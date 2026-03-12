from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <body style="font-family:Arial; max-width:600px; margin:50px auto;">
        <h1 style="color:#FF9900">🐳 Running in Docker</h1>
        <p><b>Hostname:</b> {}</p>
        <p><b>Environment:</b> {}</p>
        <p>This container is ready for cloud deployment.</p>
    </body>
    </html>
    '''.format(socket.gethostname(), os.environ.get('APP_ENV', 'development'))

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "hostname": socket.gethostname()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
