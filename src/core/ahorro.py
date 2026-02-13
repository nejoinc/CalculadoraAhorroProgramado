class AhorroProgramado:
    """
        Documentacion AhorroProgramado
        
        :param meta: La meta a la cual se desea llegar
        :type meta: float
        :param plazo: El plazo en meses para alcanzar la meta
        :type plazo: int
        :param extra: El monto extra que se desea aportar cada mes
        :type extra: float
        :return: El monto que se debe ahorrar cada mes para alcanzar la meta en el plazo establecido, considerando el aporte extra
        :rtype: float
    """ 

    def __init__(self, meta: float, plazo: int, extra: float):
        self.meta = meta
        self.plazo = plazo
        self.extra = extra
    
    def calcular_ahorro(self) -> float:
        if self.plazo == 0:
            return 0
        ahorro_base = (self.meta - self.extra * self.plazo) / self.plazo
        return round(ahorro_base, 2) if ahorro_base > 0 else 0



meta1 = AhorroProgramado(1100000, 6, 0)
print(meta1.calcular_ahorro())
    



 
    