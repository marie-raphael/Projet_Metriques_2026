from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.get("/health")
def health():
    return jsonify(status="ok")
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
