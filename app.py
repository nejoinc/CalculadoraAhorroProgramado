from flask import Flask 
from flask import render_template, request 
from src.controller.ahorro_controller import AhorroController
from src.controller.usuario_controller import UsuarioController
from src.model.ahorro import Ahorro, AhorroProgramado
from src.model.usuario import Usuario
from src.view.web import vista_ahorro
app = Flask(__name__)

app.register_blueprint(vista_ahorro.blueprint)

if __name__ == "__main__":
    app.run(debug = True )