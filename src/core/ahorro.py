from dataclasses import dataclass, field
@dataclass

class AhorroProgramado:
    """
    Documentacion AhorroProgramado
    :param tasa: La tasa de interés mensual valor constante
    :type tasa: float
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
        if self.meta <= 0: 
            raise ValueError("Error: el valor a ahorar debe ser mayor a 0")
        if self.plazo <= 0: 
            raise ValueError("Error: el plazo debe ser mayor a 0")       
        if self.mes_extra < 1 or self.mes_extra > self.plazo:
            raise ValueError("Error: el mes extra debe estar entre 1 y el plazo")          
        if self.extra > self.meta: 
            raise ValueError("Error: abono supera meta de ahorro")
        
        if self.extra == self.meta:
            return 0
        

        i = self.tasa
        n = self.plazo
        k = self.mes_extra

        if k > 0:
            fv_extra = self.extra * (1 + i)**(n - k)
        else:
            fv_extra = 0
    
        factor = ((1 + i)**n - 1) / i

        cuota = (self.meta - fv_extra) / factor

        return round(cuota, 2)

    