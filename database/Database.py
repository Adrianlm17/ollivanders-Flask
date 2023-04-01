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
        sql="SELECT id, itemType, name, sellIn, quality FROM items"
        cursor.execute(sql)
        items = cursor.fetchall()
        return items
    
    except Exception as ex:
        print(ex)
        return "Error al visualizar todos los items!"
    


# Visualizar unico Item
def ver_item(id):
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql="SELECT id, itemType, name, sellIn, quality FROM items WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        item = cursor.fetchone()
        return item
    
    except Exception as ex:
        return "Error al visualizar todos los items!"



# Añadir Item
def añadirItem(itemType, name, sellIn, quality):
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql = """INSERT INTO `items` (`itemType`, `name`, `sellIn`, `quality`) 
        VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (itemType, name, sellIn, quality))
        conexion.commit() #Confirmar acción
        return "Item añadido!"
    
    except Exception as ex:
        print(ex)
        return "Error"


# Eliminar Item
def eliminarItem(id):
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql="DELETE FROM items WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.commit() #Confirmar acción
        return "Item eliminado!"
    
    except Exception as ex:
        return jsonify({"mensaje":"Error"})
    


# Actualizar Items
def updateItem(id, sellIn, quality):
    try:
        conexion = db_connect()
        cursor = conexion.cursor()
        sql = "UPDATE items SET sellIn = %s, quality = %s WHERE id = %s"
        values = (sellIn, quality, id)
        cursor.execute(sql, values)
        conexion.commit()
        return "Items actualizados!"
    except Exception as ex:
        return "Error al actualizar items"
