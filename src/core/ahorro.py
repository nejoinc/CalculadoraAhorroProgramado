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

class ErrorExtraMenorACero(Exception): 
    """
        Se usa cuando el monto extra es menor que 0
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
        if self.meta <= 0: 
            raise ErrorMetaMayorACero("Error: el valor a ahorar debe ser mayor a 0")
        if self.plazo <= 0: 
            raise ErrorPlazoMayorACero("Error: el plazo debe ser mayor a 0")       
        if self.mes_extra < 1 or self.mes_extra > self.plazo:
            raise ErrorMesExtraFueraDelRango("Error: el mes extra debe estar entre 1 y el plazo")          
        if self.extra > self.meta: 
            raise ErrorAbonoSuperaMeta("Error: abono supera meta de ahorro")
        if self.extra < 0: 
            raise ErrorExtraMenorACero("Error: El extra es menor que 0")
        
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

    