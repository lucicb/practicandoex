

app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'     







# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)