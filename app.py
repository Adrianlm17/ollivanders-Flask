from flask import Flask, render_template, request
from database import DataBase

app = Flask(__name__)



# Prueba Conexion Base de datos
DataBase.db_connect()
print("Conexion establecida con la base de datos!")




# Index
@app.route("/")
def index():
    return render_template("ollivanders/index.html")



# Ver Inventario
@app.route("/inventario", methods=["GET"])
def inventario():
    registro = DataBase.ver_items()

    return render_template("ollivanders/items.html", registro = registro)



# Ver Item
@app.route("/inventario/<id>", methods=["GET"])
def item(id):
    
    producto = DataBase.ver_item(id)
    
    return render_template("ollivanders/item.html",  producto = producto)



# Añadir Item
@app.route("/inventario/crear", methods=["POST"])
def crear():

    tipoItem = ["NormalItem", "AgedBrie", "Conjured", "Sulfuras", "Backstage"]

    name = request.json.get("name")
    itemType = request.json.get("itemType")
    sellIn = request.json.get("sellIn")
    quality = request.json.get("quality")

    if itemType in tipoItem:

        DataBase.añadirItem(name, itemType, sellIn, quality)
        print("Item añadido!")
        return inventario()
    
    else:
        return render_template("ollivanders/errors/errorCreación.html")


# Eliminar Item
@app.route("/inventario/eliminar", methods=["DELETE"])
def eliminar():
    
    id = request.json.get("id")
    registro = DataBase.ver_item(id)

    if registro is not None:
        DataBase.eliminarItem(id)
        return inventario()
    
    else:
        return render_template("ollivanders/errors/idNotFound.html")



# Actualizar Item
@app.route("/inventario/<id>", methods=["PUT"])
def actualizar(id):

    registro = DataBase.ver_item(id)

    if id in registro:
        sellIn = request.json.get("sellIn")
        quality = request.json.get("quality")
        DataBase.updateItem(id, sellIn, quality)
        return inventario()
    
    else:
        return render_template("ollivanders/errors/idNotFound.html")
    


# ERRORES WEB
@app.errorhandler(404)
def not_found(error):
    return "<h1> La página que intentas buscar no existe...", 404

@app.errorhandler(400)
def metodo_invalido(error):
    return "<h1> Su petición es incorrecta...</h1>", 400

@app.errorhandler(405)
def metodo_no_permitido(error):
    return "<h1> Su metodo no se permite...</h1>", 405



if __name__ == "__main__":

    app.run()
