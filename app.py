from flask import Flask, render_template

# Cria uma instância do Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
