from flask import Flask
#appというFlaskクラスのインスタンスを作成。
#app.<Flaskクラスのメソッド名>とすることでFlaskクラスのメソッドを使えるようにする。
app = Flask(__name__)

#@app.route()は、次の行で定義される関数を指定した URL に対応づけるという処理するデコレーター
#app.route()の引数にはhttp://127.0.0.1:5000/以降のURLを指定します。
#すなわち、下記のコードではhttp://127.0.0.1:5000/ にアクセスした時にhello_world()関数が呼び出される
@app.route('/')
def hello_world():
    return "Hello World!"

#__name__ == '__main__'がTrueである、すなわちこのコードが直接実行されたときのみ
#app.run()が実行され、Flaskアプリが起動します。
if __name__ == "__main__":
    app.run()