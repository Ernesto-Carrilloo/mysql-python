from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)




#get -> consultar
@app.route('/productos', methods=['GET'])
def ver_productos():
    db = mysql.connector.connect(
        host='ernestocarrillo.mysql.pythonanywhere-services.com',
        user='ernestocarrillo', #mi usuario
        password='codoacodo123777', #mi contraseña
        database='ernestocarrillo$tienda' #nombre de la base de datos
    )

    cursor = db.cursor(dictionary=True) #en lugar de tener una lista con tuplas, tener un diccionario con clave(campo) y valor(dato)
    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()

    cursor.close()
    return jsonify(productos) #generamos un json como respuesta


#delete -> eliminar
#'/eliminar_producto/1' elimina el registro con id 1
#'/eliminar_producto/78' elimina el registro con id 78
#'/eliminar_producto/5' elimina el registro con id 5
@app.route('/eliminar_producto/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    db = mysql.connector.connect(
        host='ernestocarrillo.mysql.pythonanywhere-services.com',
        user='ernestocarrillo', #mi usuario
        password='codoacodo123777', #mi contraseña
        database='ernestocarrillo$tienda' #nombre de la base de datos
    )

    cursor = db.cursor()
    cursor.execute("DELETE FROM productos WHERE id = %s", (id,))

    db.commit()
    cursor.close()
    return jsonify({"mensaje":"REGISTRO ELIMINADO CON EXITO!!!"})


#post -> crear un nuevo elemento en el servidor
@app.route('/agregar_producto', methods=['POST'])
def crear_producto():
    info = request.json
    '''
    info = { "nombre": "Kiwi", "cantidad": 45 , "precio":11}
    '''
    db = mysql.connector.connect(
        host='ernestocarrillo.mysql.pythonanywhere-services.com',
        user='ernestocarrillo', #mi usuario
        password='codoacodo123777', #mi contraseña
        database='ernestocarrillo$tienda' #nombre de la base de datos
    )

    cursor = db.cursor()
    cursor.execute("INSERT INTO productos(nombre,cantidad,precio) VALUES(%s,%s,%s)", (info["nombre"],info["cantidad"],info["precio"])) #("monitor", 45 , 100500)

    db.commit()
    cursor.close()
    return jsonify({"mensaje":"REGISTRO CREADO CON EXITO!!!"})



#put -> actualizar
@app.route('/actualizar_producto/<int:id>', methods=['PUT'])
def modificar_producto(id):
    info = request.json
    '''
    info = { "nombre": "Naranja", "categoria": 33 , "precio":2}
    '''
    db = mysql.connector.connect(
        host='ernestocarrillo.mysql.pythonanywhere-services.com',
        user='ernestocarrillo', #mi usuario
        password='codoacodo123777', #mi contraseña
        database='ernestocarrillo$tienda' #nombre de la base de datos
    )

    cursor = db.cursor()
    cursor.execute("UPDATE productos SET nombre= %s, cantidad= %s, precio= %s WHERE id = %s", (info["nombre"],info["cantidad"],info["precio"] , id)) #("monitor", 45 , 100500)

    db.commit()
    cursor.close()
    return jsonify({"mensaje":"REGISTRO ACTUALIZADO CON EXITO!!!"})


if __name__ == '__main__':
    app.run(debug=True)