Pilas Engine
============ 

Pilas es un motor para realizar videojuegos de manera rápida y sencilla. 
Es una herramienta orientada a programadores casuales o principiantes, 
que quiera comenzar a realizar sus primeros videojuegos. 

http://www.pilas-engine.com.ar

Este paquete contiene Pilas Engine para Huayra GNU/Linux.

## Para generar el paquete: ##

1. uscan # para descargar la version más reciente de pilas
2. wget http://media.readthedocs.org/pdf/pilas/latest/pilas.pdf -O debian/manual.pdf  #Copiar el nuevo manual a debian/manual.pdf
3. dch -i # para actualizar el changelog, asegurarse que la versión del paquete coincida con la de pilas
4. pdebuild # generar el paquete
5. Si publicas la version generada, crea un tag en este repo :)
