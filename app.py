from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    # index.html 內會載入 avatar.jpg、style.css 並套用 Dark Mode 切換
    return render_template('index.html')


if __name__ == '__main__':
    # 啟動伺服器，預設監聽 127.0.0.1:5000
    app.run(debug=True)