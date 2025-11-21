from paquete import *

RUTA_FACIL = "nonogramas/facil/"
RUTA_MEDIO = "nonogramas/medio/"
RUTA_DIFICIL = "nonogramas/dificil/"


activo = True
while activo:
    
    opcion = mostrar_menu("Ingrese el numero de la opocion que desea: ")
    
    while not opcion.isdigit():
        opcion = mostrar_menu("ERROR, Ingresar un numero valido")
        
    
    opcion = int(opcion)
    
    match opcion:
        case 1: 
            registro = input("Ingrese el nombre con el que sera registrado: ").strip()
            
            while registro == "":
                
                registro = input("No podes dejarlo vacio. Intente nuevamente: ").strip()
            
            print(f"BIENVENIDO {registro}!!")
            print("Dificultades:")
            print("1- Facil")
            print("2- Medio")
            print("3- Dificl")
            
            dificultad = input("Elija el nivel de dificultad del nonograma (1-3): ")
            
            while not dificultad.isdigit():
                deficultad = ("ERROR, Ingrese un numero valido ")
            
            dificultad = int(dificultad)
            
            if dificultad == 1:
                ruta = elegir_nonograma_random(RUTA_FACIL)
                
            elif dificultad == 2:
                ruta = elegir_nonograma_random(RUTA_MEDIO)
            
            elif dificultad == 3:
                ruta = elegir_nonograma_random(RUTA_DIFICIL)
            else:
                print("Opcion de dificultad invalida")
                continue
            
            
            nonograma = cargar_nonograma_csv(ruta)
            
            jugar_nonograma(nonograma)
            
            
            
            
        
                
                
        
            
            
            
            
        