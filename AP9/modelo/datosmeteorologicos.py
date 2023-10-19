from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
       
        temp_sum = 0
        humedad_sum = 0
        presion_sum = 0
        viento_sum = 0
        direcciones = []  

        
        direccion_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
            "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
            "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
            "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }

        
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.startswith("Temperatura:"):
                    temp_sum += float(linea.split(":")[1])
                elif linea.startswith("Humedad:"):
                    humedad_sum += float(linea.split(":")[1])
                elif linea.startswith("Presión:"):
                    presion_sum += float(linea.split(":")[1])
                elif linea.startswith("Viento:"):
                    viento_data = linea.split(":")[1].strip().split(",")
                    velocidad = float(viento_data[0])
                    direccion = viento_data[1]
                    
                    direcciones.append(direccion_grados[direccion])

        num_registros = len(direcciones)
        if num_registros > 0:
            temp_promedio = temp_sum / num_registros
            humedad_promedio = humedad_sum / num_registros
            presion_promedio = presion_sum / num_registros
            viento_promedio = viento_sum / num_registros
         
            direccion_prominente_grados = sum(direcciones) / num_registros
            
            direccion_prominente = min(direccion_grados, key=lambda x: abs(direccion_grados[x] - direccion_prominente_grados))
        else:
            temp_promedio = 0
            humedad_promedio = 0
            presion_promedio = 0
            viento_promedio = 0
            direccion_prominente = "N/A"

        return (temp_promedio, humedad_promedio, presion_promedio, viento_promedio, direccion_prominente)
            

        

        