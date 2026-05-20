#kevin Hernan Mateus Lizcano
def calcular_y_clasificar_jornada(matriz_recursos):
    Maximo_HORAS = 40
    
    # 1. Imprimimos los títulos de las columnas bien alineados
    print(f"{'Recurso':<15} | {'Lunes':4} | {'Martes':<4} | {'Miércoles':<4} | {'Jueves':<4} | {'Viernes':<4} | {'Total':<6} | {'Clasificación'}")
    print("-" * 75)
    
    

    for fila in matriz_recursos:
        nombre = fila[0]

        # Guardamos las horas de cada día para poder mostrarlas
        lun, mar, mie, jue, vie = fila[1], fila[2], fila[3], fila[4], fila[5]
        
        # Calculamos el total de la semana
        total_horas = sum(fila[1:])
        
        # Aplicamos la lógica de negocio para clasificar
        if total_horas > Maximo_HORAS:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"
            
        # 2. Mostramos toda la información detallada por pantalla
        print(f"{nombre:<15} | {lun:<5} | {mar:<6} | {mie:<9} | {jue:<6} | {vie:<7} | {total_horas:<6} | {clasificacion}")

# Matriz con 4 recursos y sus horas de Lunes a Viernes
matriz_horas = [
    ["Ana Gómez", 8, 8, 9, 8, 8],       # Total: 41 -> Sobretiempo
    ["Carlos Pérez", 8, 7, 8, 8, 6],    # Total: 37 -> Horario Estándar
    ["María López", 9, 9, 9, 9, 8],     # Total: 44 -> Sobretiempo
    ["Juan Torres", 8, 8, 8, 8, 8]      # Total: 40 -> Horario Estándar
]

# Ejecución del módulo
calcular_y_clasificar_jornada(matriz_horas)
