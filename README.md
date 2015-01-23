python-pilas
============ 

IMPORTANTE: estos pasos ya no se utilizan para empaquetar pilas ... ver el repositorio hugoruscitti/pilas
=========================================================================================================




Empaquetado deb de Pilas Engine para Huayra GNU/Linux

Pilas es un motor para realizar videojuegos de manera rápida y sencilla. 
Es una herramienta orientada a programadores casuales o principiantes, 
que quiera comenzar a realizar sus primeros videojuegos. 

http://www.pilas-engine.com.ar

Este repositorio contiene los archivos necesarios para construir un el paquete deb de pilas para Huayra.

## Para generar el paquete: ##

Tenes que estar dentro del directorio python-pilas, y de ser
posible dentro de otro directorio temporal.

La idea de las instrucciones es que generen un directorio
llamado pilas con todos los archivos de pilas.

La estructura de archivos recomandada es:

    tmp/
     |
     |
     --- pilas/ (se genera automaticamente)   
     |
     --- python-pilas/ (este directorio)

Comandos:

    export VERSION="0.84.3"
    cd ..
    git clone http://github.com/hugoruscitti/pilas.git
    cd pilas
    git checkout $VERSION
    git submodule update --init
    tar cvzf ../python-pilas_$VERSION.orig.tar.gz *

    cd ../python-pilas
    dch -i     # (ver nota al pie *1)
    pdebuild


Notas:

1 - En el changelog tiene que coincidir con la versión exportada
en la variable VERSION
Si publicas la version generada, crea un tag en este repo :)

NOTA: Mike está armando un script para automatizar los pasos.
