class AhorroProgramado:
    """
    Documentacion AhorroProgramado
    
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

    def __init__(self, meta: float, plazo: int, extra: float, mes_extra: int):
        self.meta = meta
        self.plazo = plazo
        self.extra = extra
        self.mes_extra = mes_extra
    
    def calcular_ahorro(self) -> float:
        if self.meta < 0: 
            return "Error: el valor a ahorar debe ser mayor a  0"
        if self.plazo <= 0: 
            return "Error: el plazo debe ser mayor a 0"
        if self.mes_extra < 1 or self.mes_extra > self.plazo:
            return "Error"          
        if self.extra > self.meta: 
            return "Error: abono supera meta de ahorro"
        
        meta_restante = self.meta - self.extra

        ahorro_base = meta_restante / self.plazo
        
      
        return round(ahorro_base, 2) if ahorro_base > 0 else 0
      

    