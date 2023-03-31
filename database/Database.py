from flask import jsonify, request
from database.Config import config
import mysql.connector
import sys



# Conexion Base de datos
def db_connect():
    try:
        conexion = mysql.connector.connect(**config)
        return conexion
    
    except:
        print("Error en la conexión a la base de datos...")
        sys.exit()



# Visualizar inventario
def ver_items():
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql="SELECT id, name, sellIn, quality FROM items"
        cursor.execute(sql)
        items = cursor.fetchall()
        inventario = []
        for item in items:
            item_tienda = {'id': item[0], 'name': item[1], 'sellIn': item[2], 'quality': item[3]}
            inventario.append(item_tienda)
        return jsonify({'Item': inventario })
    
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje":"Error"})
    


# Visualizar unico Item
def ver_item(id):
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql="SELECT id, name, sellIn, quality FROM items WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        item=cursor.fetchone()
        if item != None:
            item_tienda  = {'id': item[0], 'name':item[1], 'sellIn':item[2], 'quality':item[3]}
            return jsonify({'Item': item_tienda })
        else:
            return jsonify({'mensaje': "Item no encontrado!"})
    
    except Exception as ex:
        return jsonify({"mensaje":"Error"})



# Añadir Item
def añadirItem(name, itemType, sellIn, quality):
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql = """INSERT INTO `items` (`name`, `sellIn`, `quality`) 
        VALUES ('{0}', '{1}', '{2}')""".format(request.json['name'],request.json['sellIn'],request.json['quality'])
        cursor.execute(sql)
        conexion.commit() #Confirmar acción
        return jsonify({"mensaje":"Item añadido!"})
    
    except Exception as ex:
        return jsonify({"mensaje":"Error"})   


# Eliminar Item
def eliminarItem(id):
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql="DELETE FROM items WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.commit() #Confirmar acción
        return jsonify({'mensaje': "Item eliminado!"})
    
    except Exception as ex:
        return jsonify({"mensaje":"Error"})
    


# Update Item
def updateItem(id, sellIn, quality):
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql = "UPDATE items SET sellIn = '{0}', quality = '{1}' WHERE id = '{2}'".format(request.json['sellIn'],request.json['quality'], id)
        cursor.execute(sql)
        conexion.commit() #Confirmar acción
        return jsonify({"mensaje":"Item actualizado!"})
    
    except Exception as ex:
        return jsonify({"mensaje":"Error"})   
