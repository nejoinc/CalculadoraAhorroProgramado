from flask import Blueprint 
from flask import render_template, request 
from src.controller.ahorro_controller import AhorroController
from src.controller.usuario_controller import UsuarioController
from src.model.ahorro import Ahorro, AhorroProgramado
from src.model.usuario import Usuario

blueprint = Blueprint("vista_ahorro_blue", __name__, template_folder="templates")


@blueprint.route("/")
def inicio():
    return render_template("crear_meta.html")


@blueprint.route("/crear_tablas")
def crear_tablas():
    UsuarioController.crear_tabla()
    AhorroController.crear_tabla()
    return "Tablas creadas"

@blueprint.route("/guardar-meta")
def guardar_meta():

    id_usuario = UsuarioController.obtener_siguiente_id()

    usuario_prueba = Usuario(
        id_usuario=id_usuario,
        nombre="Usuario Test Meta 2",
        email=f"test.meta2.{id_usuario}@email.com"
    )
    UsuarioController.insertar(usuario_prueba)
        
    ahorro = Ahorro(meta=float(request.args["meta"]), plazo=int(request.args["plazo"]), extra=float(request.args["extra"]), mes_extra=int(request.args["mes_extra"]))
    AhorroController.calcular_y_guardar(id_usuario, ahorro)
        

    return "Estamos guardando la meta del ahorro =  " + request.args["meta"] + " con el plazo " + request.args["plazo"]


@blueprint.route("/buscar-meta")
def buscar_meta():
    id_meta = int(request.args["meta"])
    meta = AhorroController.buscar_meta(id_meta)
    
    if meta is None:
        return f"No se encontró una meta con id {id_meta}"
    else:
        return render_template("detalle_meta.html", meta=meta)


if __name__ == "__main__":
    blueprint.run(debug = True )