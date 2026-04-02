from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>🎉 СОЦСЕТЬ soulflow08 РАБОТАЕТ!</h1><p>Регистрация и посты в разработке</p>'

@app.route('/register')
@app.route('/login')
def register():
    return '<h1>Регистрация работает!</h1>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
