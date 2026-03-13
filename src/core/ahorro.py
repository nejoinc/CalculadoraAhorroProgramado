from dataclasses import dataclass, field


class ErrorMetaMayorACero(Exception):
    """
    Se usa cuando la meta del ahorro es menor o igual que 0
    """
    pass


class ErrorPlazoMayorACero(Exception):
    """
    Se usa cuando el plazo del ahorro es igual o menor que 0
    """
    pass


class ErrorAbonoSuperaMeta(Exception):
    """
    Se usa cuando el abono extra supera la meta de ahorro
    """
    pass


class ErrorMesExtraFueraDelRango(Exception):
    """
    Se usa cuando el mes donde se hace el abono extra es mayor que la meta del ahorro programado
    """
    pass


class ErrorAbonoExtraMenorAcero(Exception):
    """
    Se usa cuando el abono extra es menor que 0
    """
    pass


@dataclass
class AhorroProgramado:
    """
    Documentacion AhorroProgramado

    :ivar tasa: La tasa de interés mensual valor constante
    :vartype tasa: float

    :param meta: La meta a la cual se desea llegar
    :type meta: float

    :param plazo: El plazo en meses para alcanzar la meta
    :type plazo: int

    :param extra: El monto extra que se desea aportar en un mes específico
    :type extra: float

    :param mes_extra: El mes en el que se hará el aporte extra
    :type mes_extra: int

    :return: El monto que se debe ahorrar cada mes para alcanzar la meta
    :rtype: float
    """

    tasa: float = field(default=0.0075, init=False)
    meta: float
    plazo: int
    extra: float
    mes_extra: int

    def calcular_ahorro(self) -> float:
        """
        Método principal que calcula la cuota mensual necesaria
        para alcanzar la meta de ahorro.
        """

        self._validar_datos()

        if self.meta == 0:
            return 0

        if self.extra == self.meta:
            return 0

        valor_futuro_extra = self._calcular_valor_futuro_extra()
        factor_anualidad = self._calcular_factor_anualidad()

        cuota_mensual = (self.meta - valor_futuro_extra) / factor_anualidad

        return round(cuota_mensual, 2)

    def _validar_datos(self):
        """
        Realiza todas las validaciones de los datos ingresados
        antes de ejecutar el cálculo financiero.
        """

        if self.meta < 0:
            raise ErrorMetaMayorACero(
                f"Error: la meta de ahorro {self.meta} ingresada debe ser mayor a 0"
            )

        if self.plazo <= 0:
            raise ErrorPlazoMayorACero(
                f"Error: el plazo {self.plazo} ingresado debe ser mayor a 0"
            )

        if self.extra < 0:
            raise ErrorAbonoExtraMenorAcero(
                f"Error: abono {self.extra} ingresado debe ser mayor que 0"
            )

        if self.extra > self.meta:
            raise ErrorAbonoSuperaMeta(
                f"Error: El extra {self.extra} ingresado supera la meta de ahorro {self.meta}"
            )

        if self.mes_extra < 1 or self.mes_extra > self.plazo:
            raise ErrorMesExtraFueraDelRango(
                f"Error: el mes extra ingresado {self.mes_extra} debe estar entre 1 y el plazo {self.plazo}"
            )

    def _calcular_valor_futuro_extra(self) -> float:
        """
        Calcula el valor futuro del abono extra considerando
        el número de meses restantes hasta el final del plazo.
        """

        meses_restantes = self.plazo - self.mes_extra

        valor_futuro_extra = self.extra * (1 + self.tasa) ** meses_restantes

        return valor_futuro_extra

    def _calcular_factor_anualidad(self) -> float:
        """
        Calcula el factor financiero correspondiente
        a una anualidad ordinaria con interés compuesto.
        """

        factor = ((1 + self.tasa) ** self.plazo - 1) / self.tasa

        return factor