from flask import Flask,render_template#Flask және render_template алу

app = Flask(__name__)#интализация Flask

@app.route('/')
def home():
    return render_template("index.html")#index.html саитка шығару Templates Фаиылында

if __name__=="__main__":
    app.run(debug=True)
