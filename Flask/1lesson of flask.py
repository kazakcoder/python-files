from flask import Flask #Flask кітапханасын алу

app = Flask(__name__)#Flask интализация
@app.route('/home')#саитка сылка роуте жасау мысалы:http://127.0.0.1:5000/home
def home():
  return "hello, World"#жазу шығару веб саита
if __name__=="__main__":
  app.run(debug=True)
