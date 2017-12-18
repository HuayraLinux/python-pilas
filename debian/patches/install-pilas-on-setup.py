Description: Install the pilas module on setup.py
 The setup.py provided in the upstream sourcecode doesn't install all the
 python modules needed for the deprecated usage of this library.
 This patch aims to fix it.
 .
 For more info on this see http://pilas-engine.com.ar/#/docs/guia_conversion
 -
Author: Ignacio Losiggio <iglosiggio@gmail.com>

--- a/setup.py
+++ b/setup.py
@@ -53,6 +53,7 @@
             'pilasengine.eventos',
             'pilasengine.interfaz',
             'pilasengine.sonidos',
+            'pilas',
             'data',
         ],
         url='http://www.pilas-engine.com.ar',
