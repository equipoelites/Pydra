## Pydra - Herramienta de Ciberseguridad

Pydra es una herramienta de ciberseguridad desarrollada en Python que proporciona diversas funcionalidades para realizar tareas relacionadas con la seguridad informática. Esta herramienta está diseñada para propósitos educativos y de pruebas de seguridad autorizadas. No debe utilizarse para realizar actividades ilegales o dañinas.

### Características

- Cifrado de contraseñas: Pydra utiliza el módulo `cryptography` para cifrar contraseñas de forma segura.
- Escaneo de puertos: Permite escanear puertos en una dirección IP especificada para identificar puertos abiertos.
- Ataque de fuerza bruta: Implementa un ataque de fuerza bruta mediante SSH utilizando la biblioteca `paramiko`.
- Conexión a través de Tor: Ofrece la opción de realizar conexiones a través de la red Tor utilizando el módulo `socks` de `requests`.

### Requisitos

- Python 3.x instalado.
- Instalación de los siguientes paquetes: `cryptography`, `wxPython`, `requests`, `socks`, `paramiko`.

### Instalación

1. Clonar este repositorio en tu sistema local:

```
git clone https://github.com/tu_usuario/pydra.git
```

2. Instalar las dependencias necesarias:

```
pip install cryptography wxPython requests socks paramiko
```

### Uso

Ejecuta el archivo `pydra.py` para abrir la interfaz gráfica de usuario (GUI) de Pydra. A través de esta GUI, podrás realizar las siguientes acciones:

1. Cifrar contraseñas: Ingresa una contraseña en el cuadro de texto y haz clic en "Cifrar contraseña" para obtener la versión cifrada.

2. Escaneo de puertos: Introduce la dirección IP y el puerto que deseas escanear y haz clic en "Escaneo de puertos" para obtener los puertos abiertos en la dirección IP especificada.

3. Ataque de fuerza bruta: Ingresa una dirección IP y una contraseña, luego haz clic en "Ataque de fuerza bruta" para intentar iniciar sesión en el sistema utilizando el ataque de fuerza bruta.

4. Conexión a través de Tor: Puedes seleccionar la opción "Conexión a través de Tor" antes de realizar cualquier operación para ocultar tu dirección IP detrás de la red Tor.

### Advertencia

El uso de Pydra para cualquier propósito malicioso o ilegal está estrictamente prohibido. Asegúrate de obtener el permiso explícito del propietario de los sistemas o redes antes de realizar pruebas de seguridad o cualquier actividad relacionada. Los autores de Pydra no se hacen responsables por ningún uso indebido o ilegal de esta herramienta.

### Contribuciones

Las contribuciones a Pydra son bienvenidas. Si deseas contribuir con mejoras, correcciones de errores o nuevas características, por favor crea una rama con tu nombre de usuario y envía una solicitud de extracción.
