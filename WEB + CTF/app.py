from flask import Flask, render_template, request
import threading
import webbrowser

app = Flask(__name__)
access_code = None

def fake_ssh_server():
    global access_code
    access_code = "8ibQ~78N"  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_code', methods=['POST'])
def check_code():
    global access_code
    entered_code = request.form.get('code', '')
    if entered_code == access_code:
        return "Accès autorisé. Flag : GG{v0tre_fl@g}"
    else:
        return "Accès refusé. Code incorrect."

@app.route('/get_access_code', methods=['GET'])
def get_access_code():
    global access_code
    authentication_key = request.args.get('auth_key', '')
    if authentication_key == 'B3':
        return access_code
    else:
        return "Clé d'authentification incorrecte."

def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    ssh_thread = threading.Thread(target=fake_ssh_server)
    ssh_thread.start()

    # Ouvrir le navigateur dans un thread séparé
    threading.Timer(1, open_browser).start()

    app.run(debug=False)
