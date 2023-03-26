from flask import Flask, jsonify, request
import mysql.connector
from database.Database import config


app = Flask(__name__)

conexion = mysql.connector.connect(**config)


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





# ERRORES WEB
def not_found(error):
    return "<h1> La página que intentas buscar no existe...", 404





if __name__ == "__main__":
    
    # ERRORES
    app.register_error_handler(404, not_found)
    
    # RUN (automaticamente)
    app.run()
