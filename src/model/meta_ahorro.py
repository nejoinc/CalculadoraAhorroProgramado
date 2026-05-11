from dataclasses import dataclass


@dataclass
class MetaAhorro:
    id_meta: int | None = None
    id_usuario: int = 0
    meta: float = 0.0
    plazo: int = 0
    extra: float = 0.0
    mes_extra: int = 0
    tasa: float = 0.0075
    cuota_mensual: float | None = None
    fecha_calculo: str = ""
