python-pilas
============ 

Empaquetado deb de Pilas Engine para Huayra GNU/Linux

Pilas es un motor para realizar videojuegos de manera rápida y sencilla. 
Es una herramienta orientada a programadores casuales o principiantes, 
que quiera comenzar a realizar sus primeros videojuegos. 

http://www.pilas-engine.com.ar

Este repositorio contiene los archivos necesarios para construir un el paquete deb de pilas para Huayra.

## Para generar el paquete: ##

1. uscan # para descargar la version más reciente de pilas
2. dch -i # para actualizar el changelog, asegurarse que la versión del paquete coincida con la de pilas
3. pdebuild # generar el paquete
4. Si publicas la version generada, crea un tag en este repo :)
