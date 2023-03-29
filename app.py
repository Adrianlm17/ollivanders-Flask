from flask import Flask


app = Flask(__name__)




# ERRORES WEB
def not_found(error):
    return "<h1> La página que intentas buscar no existe...", 404





if __name__ == "__main__":
    
    # ERRORES
    app.register_error_handler(404, not_found)
    
    # RUN (automaticamente)
    app.run()
