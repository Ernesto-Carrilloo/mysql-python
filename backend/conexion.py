from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

#get -> consultar
#post -> crear un nuevo elemento en el servidor
#delete -> eliminar
#put -> actualizar

#consultar
@app.route('/productos', methods=['GET'])
def ver_productos():
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='ernesto', #mi contraseña
        database='sys' #nombre de la base de datos
    )
    
    cursor = db.cursor(dictionary=True) #en lugar de tener una lista con tuplas, tener un diccionario con clave(campo) y valor(dato)
    cursor.execute("SELECT * FROM productos")
    
    productos = cursor.fetchall()
    
    cursor.close()
    return jsonify(productos) #generamos un json como respuesta
    
if __name__ == '__main__':
    app.run(debug=True) 