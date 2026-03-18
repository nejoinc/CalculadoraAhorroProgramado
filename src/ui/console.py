import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from model.ahorro import * 

def main():
    print("\n📈 CALCULADORA DE AHORRO PROGRAMADO\n")

    try:
        meta = float(input("Ingrese la meta de ahorro: "))
        plazo = int(input("Ingrese el plazo en meses: "))
        extra =  float(input("Ingrese el monto extra (0 si no aplica): "))
        if extra == 0:  
            mes_extra = 1
        else: 
            mes_extra = int(input("Ingrese el mes del aporte extra: "))
        
        ahorro = Ahorro(
            meta=meta,
            plazo=plazo,
            extra=extra,
            mes_extra=mes_extra
        )

        ap = AhorroProgramado()
        cuota = ap.calcular_ahorro(ahorro)

        print("\n✅ RESULTADO")
        print(f"Debes ahorrar mensualmente: ${round(cuota, 2)}")
    
    except ValueError:
        print("\n🚨 Debes ingresar valores numéricos válidos.")

    except (
        ErrorMetaMayorACero,
        ErrorPlazoMayorACero,
        ErrorAbonoSuperaMeta,
        ErrorMesExtraFueraDelRango
    ) as variableerror:
        print(f"\n🚨 {variableerror}")

    except Exception as e:
        print(f"\n⚠ Error inesperado: {e}")


if __name__ == "__main__":
    main()