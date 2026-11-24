@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  where python >nul 2>nul
  if errorlevel 1 (
    echo No se encontro Python. Instala Python 3.10 o superior desde python.org y marca "Add Python to PATH".
    echo Despues vuelve a ejecutar este archivo.
    pause
    exit /b 1
  )
  set "PYTHON=python"
) else (
  set "PYTHON=py"
)
if not exist ".venv\Scripts\python.exe" %PYTHON% -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 (
  echo No se pudieron instalar las dependencias. Revisa tu conexion a internet.
  pause
  exit /b 1
)
.venv\Scripts\python.exe main.py
pause
