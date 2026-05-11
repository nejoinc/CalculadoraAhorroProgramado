from dataclasses import dataclass


@dataclass
class Usuario:
    id_usuario: int | None = None
    nombre: str = ""
    email: str = ""
    fecha_registro: str = ""
