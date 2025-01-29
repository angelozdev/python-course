def obtener_salario_base() -> int:
    """Solicita al usuario el salario base en COP y valida la entrada."""
    while True:
        try:
            salario = int(input("Ingrese el salario base (COP): "))
            if salario < 0:
                raise ValueError("El salario no puede ser negativo.")
            return salario
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtelo de nuevo.")
        except KeyboardInterrupt:
            print("\nProceso interrumpido. Saliendo...")
            exit()


def calcular_deducciones_empleado(salario_base: int) -> dict[str, float]:
    """Calcula las deducciones que el empleado paga."""
    return {"salud": salario_base * 0.04, "pension": salario_base * 0.04}


def calcular_deducciones_empleador(salario_base: int) -> dict[str, float]:
    """Calcula las deducciones que el empleador paga."""
    return {
        "salud_empleador": salario_base * 0.085,
        "pension_empleador": salario_base * 0.12,
        "cesantias": salario_base * 0.0833,
        "intereses_cesantias": salario_base * 0.0833 * 0.12,
        "prima": salario_base * 0.0833,
        "vacaciones": salario_base * 0.0417,
        "arl": salario_base * 0.0052,
        "caja_compensacion": salario_base * 0.04,
    }


def mostrar_deducciones(
    salario_base: int,
    deducciones_empleado: dict[str, float],
    deducciones_empleador: dict[str, float],
):
    """Muestra en pantalla las deducciones calculadas."""
    print(f"Salario base: {salario_base:,.0f} COP\n")
    print(f"Salud (Empleado): {deducciones_empleado['salud']:,.0f} COP")
    print(f"Pensión (Empleado): {deducciones_empleado['pension']:,.0f} COP\n")

    for key, value in deducciones_empleador.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value:,.0f} COP")

    total_empleador = sum(deducciones_empleador.values())
    print(f"\nDeducciones totales del empleador: {total_empleador:,.0f} COP")


def calcular_total_mensual(
    salario_base: int, deducciones_empleador: dict[str, float]
) -> int:
    """Calcula el salario mensual total incluyendo deducciones del empleador."""
    return int(salario_base) + int(sum(deducciones_empleador.values()))


def convertir_usd_a_cop(cantidad_usd: float, tasa_cambio: float) -> float:
    """Convierte una cantidad en USD a COP utilizando una tasa de cambio."""
    return cantidad_usd * tasa_cambio


def convertir_cop_a_usd(cantidad_cop: float, tasa_cambio: float) -> float:
    """Convierte una cantidad en COP a USD utilizando una tasa de cambio."""
    return cantidad_cop / tasa_cambio


def calcular_perks(dolar_hoy: float) -> float:
    """Calcula los beneficios adicionales en COP."""
    perks_usd = {
        "uber": 30,
        "comida": 45,
        "computador": 500 / 36,  # Pro-rateado a 3 años
        "herramientas": 250 / 12,
        "meets": 250 / 12,
    }

    perks_cop = {
        key: convertir_usd_a_cop(value, dolar_hoy) for key, value in perks_usd.items()
    }
    perks_cop.update({"salud": 450_000, "deporte": 70_000, "streaming": 120_000})

    return sum(perks_cop.values())


def main():
    # Configuración inicial
    dolar_hoy = 4164.47

    # Entrada de datos
    salario_base = obtener_salario_base()
    salario_usd_mensual = float(input("Ingrese el salario mensual en USD: "))

    # Cálculos
    deducciones_empleado = calcular_deducciones_empleado(salario_base)
    deducciones_empleador = calcular_deducciones_empleador(salario_base)
    salario_cop_mensual = calcular_total_mensual(salario_base, deducciones_empleador)
    perks_cop = calcular_perks(dolar_hoy)

    salario_total_cop_mensual = (
        salario_cop_mensual
        + perks_cop
        + convertir_usd_a_cop(salario_usd_mensual, dolar_hoy)
    )
    salario_total_usd_mensual = salario_total_cop_mensual / dolar_hoy

    salario_neto_cop_mensual = (
        salario_total_cop_mensual
        - sum(deducciones_empleado.values())
        - sum(deducciones_empleador.values())
        - perks_cop
    )

    salario_neto_usd_mensual = salario_neto_cop_mensual / dolar_hoy

    # Resultados
    mostrar_deducciones(salario_base, deducciones_empleado, deducciones_empleador)

    print(f"\nTotal perks: {perks_cop:,.0f} COP")

    print("\n--- Resumen (NETO) ---")

    print(f"Salario neto mensual: {salario_neto_cop_mensual:,.0f} COP")
    print(f"Salario neto mensual: {salario_neto_usd_mensual:,.2f} USD")

    print("\n--- Resumen (BRUTO)---")

    print(f"Salario total mensual: {salario_total_cop_mensual:,.0f} COP")
    print(f"Salario total mensual: {salario_total_usd_mensual:,.2f} USD")


if __name__ == "__main__":
    main()
