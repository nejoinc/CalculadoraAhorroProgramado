from dataclasses import dataclass


@dataclass
class HistorialCalculo:
    id_historial: int | None = None
    id_usuario: int = 0
    meta: float = 0.0
    plazo: int = 0
    extra: float = 0.0
    mes_extra: int = 0
    tasa: float = 0.0075
    valor_futuro_extra: float | None = None
    factor_anualidad: float | None = None
    cuota_mensual: float = 0.0
    fecha_calculo: str = ""
