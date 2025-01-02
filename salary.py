salario_base: int

while True:
    try:
        salario_base = int(input("Ingrese el salario base (COP): "))
        if salario_base < 0:
            raise ValueError("El salario no puede ser negativo.")
        break  # Sale del bucle si todo está bien
    except ValueError as e:
        print(f"Entrada inválida: {e}. Inténtelo de nuevo.")
    except KeyboardInterrupt:
        print("\nProceso interrumpido. Saliendo...")
        exit()  # Sale del programa

# Lo que paga el empleado
pension = salario_base * 0.04
salud = salario_base * 0.04

# Lo que paga el empleador
salud_empleador = salario_base * 0.085
pension_empleador = salario_base * 0.12
cesantias = salario_base * 0.0833
intereses_cesantias = cesantias * 0.12
prima = salario_base * 0.0833
vacaciones = salario_base * 0.0417
arl = salario_base * 0.0052
caja_compensacion = salario_base * 0.04


deducciones_empleador = (
    salud_empleador
    + pension_empleador
    + cesantias
    + intereses_cesantias
    + prima
    + vacaciones
    + arl
    + caja_compensacion
)

print(f"Salud: {salud:,.0f} COP")
print(f"Pensión: {pension:,.0f} COP")

print("\n")

print(f"Cesantías: {cesantias:,.0f} COP")
print(f"Intereses Cesantías: {intereses_cesantias:,.0f} COP")
print(f"Salud empleador: {salud_empleador:,.0f} COP")
print(f"Pensión empleador: {pension_empleador:,.0f} COP")
print(f"ARL: {arl:,.0f} COP")
print(f"Caja de compensación: {caja_compensacion:,.0f} COP")
print(f"Deducciones empleador: {deducciones_empleador:,.0f} COP")
print(f"Salario base: {salario_base:,.0f} COP")
print(f"Salario total: {salario_base + deducciones_empleador:,.0f} COP")
print("\n")

# Datos
salario_cop_mensual = salario_base + deducciones_empleador  # Salario en COP mensual
salario_usd_mensual = int(
    input("Ingrese el salario en USD: ")
)  # Salario en USD mensual
dolar_hoy: float = 4_386.97  # Tasa de cambio actual

# Perks mensuales
uber_usd = 30
salud_cop = 450_000
comida_usd = 45
deporte_cop = 70_000

# Perks anuales
computador_usd = 500 / 3  # Cada 3 años
herramientas_usd = 250
meets_usd = 250

# Streaming (aproximado)
streaming_cop = 100_000  # Estimado mensual

# Conversión de USD a COP
uber_cop = uber_usd * dolar_hoy
comida_cop = comida_usd * dolar_hoy
computador_cop = (computador_usd * dolar_hoy) / 12
herramientas_cop = (herramientas_usd * dolar_hoy) / 12
meets_cop = (meets_usd * dolar_hoy) / 12

total_perks_cop = (
    uber_cop
    + salud_cop
    + comida_cop
    + deporte_cop
    + streaming_cop
    + computador_cop
    + herramientas_cop
    + meets_cop
)

# Cálculo del total mensual
salario_total_cop_mensual = (
    salario_cop_mensual + total_perks_cop + (salario_usd_mensual * dolar_hoy)
)

salario_total_usd_mensual = salario_total_cop_mensual / dolar_hoy
salario_total_anual_cop = salario_total_cop_mensual * 12
salario_toal_anual_usd = salario_total_usd_mensual * 12


print(f"Total perks: {total_perks_cop:,.0f} COP")
print(f"Salario total mensual: {salario_total_cop_mensual:,.0f} COP")
print(f"Salario total anual:   {salario_total_anual_cop:,.0f} COP")
print(f"Salario total mensual: {salario_total_usd_mensual:,.0f} USD")
print(f"Salario total anual:   {salario_toal_anual_usd:,.0f} USD")
