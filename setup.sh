#!/bin/bash

echo "Bienvenido a Pydra - Instalación y configuración"
echo "==============================================="

# Comprobar si Python 3.x está instalado
if ! command -v python3 &>/dev/null; then
    echo "Python 3.x no está instalado. Por favor, instala Python 3.x antes de continuar."
    exit 1
fi

# Instalar las dependencias necesarias
echo "Instalando las dependencias..."
python3 -m pip install cryptography wxPython requests socks paramiko

# Comprobar si la instalación fue exitosa
if [ $? -eq 0 ]; then
    echo "Instalación completada con éxito."
else
    echo "Ha ocurrido un error durante la instalación. Por favor, verifica las dependencias e inténtalo nuevamente."
    exit 1
fi

echo ""
echo "¡Pydra se ha instalado correctamente! Puedes ejecutar 'python3 pydra.py' para iniciar la herramienta."
