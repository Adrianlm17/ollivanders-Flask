from flask import Flask, jsonify, request
import mysql.connector
from database.Database import config
import sys


app = Flask(__name__)

# Conexion base de datos
try:
    conexion = mysql.connector.connect(**config)
    print("¡Conexión establecida!")
except:
    print("Error en la conexión a la base de datos...")
    sys.exit()



# VER ITEMS
@app.route("/")
def ver_items():
    try:
        cursor = conexion.cursor()
        sql="SELECT id, name, sellIn, quality FROM items"
        cursor.execute(sql)
        items=cursor.fetchall()
        inventario = []
        for item in items:
            item_tienda={'id': item[0], 'name':item[1], 'sellIn':item[2], 'quality':item[3]}
            inventario.append(item_tienda)
        return jsonify({'inventario': inventario})
    
    except Exception as ex:
        return jsonify({"mensaje":"Error"})


@app.route("/newItem", methods=['POST'])
def añadirItem():
    # print(request.json)
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO `items` (`name`, `sellIn`, `quality`) 
        VALUES ('{0}', '{1}', '{2}')""".format(request.json['name'],request.json['sellIn'],request.json['quality'])
        cursor.execute(sql)
        conexion.commit() #Confirmar acción
        return jsonify({"mensaje":"Item añadido!"})
    
    except Exception as ex:
        return jsonify({"mensaje":"Error"})   


# ERRORES WEB
def not_found(error):
    return "<h1> La página que intentas buscar no existe...", 404





if __name__ == "__main__":
    
    # ERRORES
    app.register_error_handler(404, not_found)
    
    # RUN (automaticamente)
    app.run()
