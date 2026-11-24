# Aplicación de ejercicios — Flask

## Requisitos

Python 3.10 o superior. Si no está instalado, instálalo desde [python.org](https://www.python.org/downloads/) y activa la opción **Add Python to PATH**.

## Ejecutar en Windows

Haz doble clic en `Iniciar.bat`. El archivo crea el entorno virtual, instala Flask y ejecuta la aplicación. Luego abre http://127.0.0.1:5000 en el navegador. Para detenerla, cierra la ventana o pulsa Ctrl+C.

También puedes ejecutarla manualmente en PowerShell desde esta carpeta:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

## Ejecutar en macOS o Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Funciones

- **Ejercicio 1:** promedio de tres notas (10 a 70) y estado de aprobación según promedio mínimo 40 y asistencia mínima 75%.
- **Ejercicio 2:** compara tres nombres e informa el más largo y su cantidad de caracteres.
