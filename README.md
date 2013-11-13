python-pilas
============ 

Empaquetado deb de Pilas Engine para Huayra GNU/Linux

Pilas es un motor para realizar videojuegos de manera rápida y sencilla. 
Es una herramienta orientada a programadores casuales o principiantes, 
que quiera comenzar a realizar sus primeros videojuegos. 

http://www.pilas-engine.com.ar

Este repositorio contiene los archivos necesarios para construir un el paquete deb de pilas para Huayra.

## Para generar el paquete: ##

0. export VERSION="0.83"
1. cd
1. git clone http://github.com/hugoruscitti/pilas.git
2. cd pilas
3. git checkout $VERSION
4. git submodule update --init
5. tar cvzf ../python-pilas_$VERSION.orig.tar.gz *
6. cd ../python-pilas
7. dch -i # para actualizar el changelog, asegurarse que la versión del paquete coincida con la de pilas
8. pdebuild # generar el paquete


Si publicas la version generada, crea un tag en este repo :)

NOTA: Mike está armando un script para automatizar los pasos.
