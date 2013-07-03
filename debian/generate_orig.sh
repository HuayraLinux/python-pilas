#!/bin/bash

git clone git@github.com:hugoruscitti/pilas.git
cd pilas
VERSION=`git tag | tail -n 1`

if [ ! $1 == "" ];
then
	VERSION=$1
fi

git checkout $VERSION
git submodule init
git submodule update
cd lanas
git submodule init
git submodule update
cd ..
tar cvzf ../../../python-pilas_$VERSION.orig.tar.gz *
cd ..
rm -rf pilas
