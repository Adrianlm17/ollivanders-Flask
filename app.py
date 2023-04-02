from flask import Flask, render_template, request
from database.Database import *
from domain.GildedRose import *

app = Flask(__name__)



# Prueba Conexion Base de datos
db_connect()
print("Conexion establecida con la base de datos!")




# Index
@app.route("/")
def index():
    return render_template("ollivanders/index.html")




# Ver Inventario
@app.route("/items", methods=["GET"])
def inventario():
    
    items = ver_items()

    return render_template("ollivanders/items.html", items = items)




# Ver Item
@app.route("/item", methods=["GET", "POST"])
def item():
    
    if request.method == "POST":
        item_id = request.form.get("id")
        producto = ver_item(item_id)
    
        if producto:
            return render_template("ollivanders/item.html",  producto = producto)
        
        else:
            return render_template("ollivanders/errors/idNotFound.html")
    
    else:
        return render_template("ollivanders/item.html")




# Crear Item
@app.route("/crear", methods=["GET", "POST"])
def crear():

    if request.method == "POST":

        tipoItem = ["NormalItem", "AgedBrie", "Conjured", "Sulfuras", "Backstage"]

        itemType = request.form.get("itemType")
        name = request.form.get("name")
        sellIn = request.form.get("sellIn")
        quality = request.form.get("quality")

        if itemType in tipoItem:

            añadirItem(itemType, name, sellIn, quality)
            print("Item añadido!")
            return inventario()
        
        else:
            return render_template("ollivanders/errors/tipoErroneo.html")
    
    else:
        return render_template("ollivanders/crear.html")



# Eliminar Item
@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    
    registro = ver_item(id)

    if registro is not None:
        eliminarItem(id)
        return inventario()
    
    return render_template("ollivanders/idNotFound.html")



# Actualizar Items
@app.route("/actualizar", methods=["PUT"])
def actualizar():
    items = ver_items()
    
    for item in items:
        itemType = item[1]
        itemName = item[2]
        itemSellIn = item[3]
        itemQuality = item[4]
        
        if itemType == "AgedBrie":
            item_obj = AgedBrie(itemName, itemSellIn, itemQuality)
        elif itemType == "Backstage":
            item_obj = BackstagePasses(itemName, itemSellIn, itemQuality)
        elif itemType == "Conjured":
            item_obj = Conjured(itemName, itemSellIn, itemQuality)
        elif itemType == "Sulfuras":
            item_obj = Sulfuras(itemName, itemSellIn, itemQuality)
        else:
            item_obj = NormalItem(itemName, itemSellIn, itemQuality)
        
        item_obj.updateQuality()
        updateItem(item[0], item_obj.sellIn, item_obj.quality)
    
    return inventario()



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

    app.run(debug=True)

