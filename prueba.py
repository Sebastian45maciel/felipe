import re
import sys
from typing import List, Tuple

class ProcesadorCorreos:
    def __init__(self, archivo: str):
        """
        Inicializa el procesador de correos con la ruta del archivo
        
        Args:
            archivo (str): Ruta al archivo que contiene los correos
        """
        self.archivo = archivo
        self.patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    def leer_archivo(self) -> List[str]:
        """
        Lee el archivo de texto y retorna una lista con las líneas
        
        Returns:
            List[str]: Lista de líneas del archivo
        """
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                return f.readlines()
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{self.archivo}'")
            sys.exit(1)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            sys.exit(1)
    
    def validar_correo(self, correo: str) -> bool:
        """
        Valida si una cadena tiene formato de correo electrónico válido
        
        Args:
            correo (str): Correo electrónico a validar
            
        Returns:
            bool: True si es válido, False si no
        """
        return bool(re.match(self.patron_email, correo.strip()))
    
    def procesar_correos(self) -> Tuple[List[str], List[str]]:
        """
        Procesa el archivo y separa los correos válidos de los inválidos
        
        Returns:
            Tuple[List[str], List[str]]: Tupla con (correos válidos, correos inválidos)
        """
        lineas = self.leer_archivo()
        validos = []
        invalidos = []
        
        for linea in lineas:
            correo = linea.strip()
            if correo:  # Ignora líneas vacías
                if self.validar_correo(correo):
                    validos.append(correo)
                else:
                    invalidos.append(correo)
        
        return validos, invalidos
    
    def guardar_resultados(self, validos: List[str], invalidos: List[str]):
        """
        Guarda los resultados en archivos separados
        
        Args:
            validos (List[str]): Lista de correos válidos
            invalidos (List[str]): Lista de correos inválidos
        """
        try:
            with open('correos_validos.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(validos))
            
            with open('correos_invalidos.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(invalidos))
                
            print(f"Se encontraron {len(validos)} correos válidos y {len(invalidos)} inválidos")
            print("Los resultados se han guardado en 'correos_validos.txt' y 'correos_invalidos.txt'")
        
        except Exception as e:
            print(f"Error al guardar los resultados: {e}")
            sys.exit(1)

def main():
    """
    Función principal que ejecuta el programa
    """
    if len(sys.argv) != 2:
        print("Uso: python programa.py archivo_correos.txt")
        sys.exit(1)
    
    procesador = ProcesadorCorreos(sys.argv[1])
    validos, invalidos = procesador.procesar_correos()
    procesador.guardar_resultados(validos, invalidos)

if __name__ == "__main__":
    main()