# mat-enm

[![PyPI version](https://img.shields.io/pypi/v/mat-enm?color=brightgreen&label=PyPI%20package)](https://pypi.org/project/mat-enm/)
[![Python Version](https://img.shields.io/pypi/pyversions/vertica-python.svg)](https://www.python.org/downloads/)

## Lista de contenido

* [Descripcion](#descripcion)
* [Instalacion](#instalacion)
* [Uso](#uso)
  * [Cargar nuevo elemento](#cargar-nuevo-elemento)
  * [Crear un conector](#crear-un-conector)
  * [Ejemplos de uso](#ejemplos-de-uso)
  

## Descripcion
"mat_enm" es un cliente de MAT diseñado específicamente para interactuar de manera sencilla y segura con gestores de Ericcson. Esta herramienta actúa como un envoltorio (wrapper) de la biblioteca "enmscripting", brindando una capa adicional de funcionalidad y comodidad para los usuarios.

Al utilizar "mat_enm", los usuarios pueden aprovechar las capacidades del gestor ENM de manera más amigable y accesible.

Además, "mat_enm" garantiza la seguridad de las credenciales en de los usuarios, utilizando mecanismos de autenticación y encriptación para proteger la integridad de los datos y prevenir accesos no autorizados.


## Instalacion

```
mat py install --index-url https://pypi.org/project/ --no-deps mat-enm
```

## Uso

Previo al la creacion de un conector es necesario contar con un Network Element en MAT.

### Cargar nuevo elemento
Para cargar un nuevo ENM en MAT, configurar las credenciales y variables de entorno necesarias, sigue estos pasos:

1. Ve a la pestaña "Network Automation" en el menú principal de MAT.
2. Selecciona "Network Elements" y luego "New Network Element".
3. En la ventana que aparece, ingresa el nombre del host (Hostname) y la dirección IP de gestión (Management IP) del ENM.
4. En la sección "Network Role", selecciona "ENM" para indicar que se trata de un elemento de red de este tipo.
5. En la sección "Stored Credentials", puedes seleccionar "MAT Credentials" para evitar tener que seleccionar manualmente las credenciales cada vez que se instancie un nuevo conector.
6. Además, es necesario agregar dos variables de entorno: el puerto (port) y el nombre de la base de datos por defecto (database). Si el puerto no se especifica, se tomará el valor predeterminado 5433.

### Crear un conector

El ejemplo que se muestar a continuacion muestra como crear un conector.

```
import mat_enm

client = mat_enm.ENMClient(ne_hostname, stored_credentials)
```

| Parametro | Description |
| --- | --- |
| ne_hostname | Network Elemet de MAT con la conexion a la base de datos <br>**Obligatorio** |
| stored_credentials | Credenciales del usuario del gestor. En caso de no estar especificado usa las del NE. <br>**Opcional** |

### Ejemplos de uso

Un caso de uso tipico para la ejecucion de un comando en el gestor podria ser el siguinete.

```
res = client.execute_command('cmedit get * networkelement.(netype==*)')
output = res.get_output()
```