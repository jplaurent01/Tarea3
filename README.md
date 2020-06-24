# Tarea3
Solución tarea 3 B63761
=======================

1) A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

Se obtiene que apartir de los datos obtenidos curvas del tipo gaussiana para las funciones de densidad marginales de X y Y, a apartir de dichas curvas de ajuste, se obtiene a través de la curva de mejor ajuste los siguiente parámetros para fx mu = 9.90484381 y sigma = 3.29944287 y para fy mu = 15.0794609 y sigma = 6.02693776.

2) Asumir independencia de X y Y, ¿cuál es entonces la función de densidad conjunta que modela los datos?

Luego de asumir independeicia de X y Y, a partir de los parámetros obtenidos en el inciso anterior, se implementa para la función fx los parámetros son mu=9.90484381 y sigma = 3.29944287 y para la función fy , se utilizan los siguientes parámetoros mu = 15.0794609 y sigma = 6.02693776, con base en lo comentado se prodece a obtener de manera analítica la función de densidad conjunta que modela los datos, con base en lo anterior se obtiene el siguiente resultado obtenido de manera analítica:

![abc](abc.png)

3) Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.

* Correlación: Se obtiene que Rxy = E[xy]  = 149.54281000000012, en términos generales la correlación indica el grado en X y Y, se encuentran linealmene asociadas , es decir es una medida que indica que tanto se parecen estas dos variables aleatorias.  

* Covarianza: Se obtiene que Cxy  = 0.06669156988847706 . La covarianza es una medida del nivel de variación conjunta entre dos variables aleatorias con base en sus medias. Cabe destacar que a pastir de dicho valor es posible hallar la dependencia o independencia entre dos variables aleatorias, por consiguiente un resultado de cero indica independencia, ya que la covarianza obtenida es muy pequeña, es decir es casi cero, se puede asegurar que X y Y son independientes.

* Coeficiente de correlación (Pearson): p = 0.003353772672199657. El coeficiente de de correlación es una medición de la dependencia  de las dos variables aleatorias, por consiguiente es un indicativo de la correlación entre las variables aleatrias, por lo tanto para p = 0, no existe una relación lineal. Con respecto al resultado experimental obtenido se observa que tiende a cero, por ende dicho valor es un indicativo de independencia lineal.


4) Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).
A continuación se muestrán las funciones de densidad marginales (2D)
![c](c.png)

En la imagen de la Figura 1, se observa la función de densidad marginal de fx obtenida de los datos reales.
![b](b.png)

En la imagen de la Figura 2, se observa la superposición entre la función de densidad marginal de fx con la curva de mejor ajuste para fx.
![f](f.png)

En la imagen de la Figura 3, se observa la función de densidad marginal de fy obtenida de los datos reales.

![d](d.png)

En la imagen de la Figura 4, se observa la superposición entre la función de densidad marginal de fy con la curva de mejor ajuste para fy.

![e](e.png)

En la imagen de la Figura 5, se observa la función de densidad conjunta obtenida a partir de los parámetros de la curva de mejor ajuste para fx y fy .








