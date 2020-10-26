# Shark Attacks!
> Proyecto: Entender los problemas potenciales de la base de datos y 'limpiarlos' para producir un data set apto de análisis.

## Breve descripción
El **README** lo destinare a dos etapas que pienso involucrar en el desarrollo del proyecto:
1. [**Inicio del proyecto**] Iniciar el desarrollo de la actividad con entender la base de datos y escribir que metodologias de tratamiento/limpieza se me ocurren con solo visualizar la base de datos desde excel.
2. [**Finalización**] Finalizado el ejericio de tratamiento, limpieza y exportado, volver a editar este documento para plantear los cambios que se hayan efectuado durante el trabajo.

## [**Inicio del proyecto**] Entendimiento y planeación
**¿La base de datos de que es?**
Es información recolectada hasta el 2018 de tiburones que han efectuado ataques contra personas en el mundo. De manera muy abierta, la base de datos registra la fecha y hora del evento, actividad que realizaba la victima, ubicación, nombre, genero y edad de la victima, etc.

**Las relaciones que encuentro de antemano entre las distintas columnas son:**
1. Desde excel puedo evidencia que de la fila **6304** en adelante son espación vacios que se pueden remover.
2. Encuentro casos muy fictys que por mi eliminaria, por ejemplo todos los que no registran fecha son basados como en estudios arqueologicos que añaden ruido al analisis que se quiera realizar. No son datos precisos y estan muy incompletos.
3. En todas las columnas, los datos vacios si no son "mapeables" entonces llenarlo con "sin especificar"
4. Identificar si un dato es mapeable o no se puede definir de diferentes formas según sea necesario:
	1. Realizar un **unique()**, si solo son caracteres especiales entonces remplazar con "sin especificar"
	2. En el caso de la hora, si dice la cadena tiene un afternoon o morning entonces normalizarlo.
	3. En el caso de genera identificar si por medio del nombre es posible mapearlo.
5. La columna de **Activity** remover los ing y convertirlo a mayuscula.
6. La columna de **Species** quitar numeros, caracteres especiales y letras solas (que no hagan parte de una palabra)
7. **Case Number**[0], **Date**, **Year**, **Time**, **Case Number**[19], **Case Number**[20] son la misma información relevante a la fecha y hora del evento. Se podría unificar en una misma columna con tipo de dato DateTime de pandas. Los primeros datos capturados evidencian fechas 
8. Unificados los anteriores elementos, podría re-asignar la columna **Original order** con precisión y otrogarle el atributo de indice para filas con tipo INT.
9. Unificar las columnas **pdf**, **href**, y **href formula**.
10. Evaluar si existen datos vacios en **Country**, **Area** o **Location** convertirlo a "Sin especificar".
11. Si el tiempo me da y soy muy pro, podría reunir las columnas **Country**, **Area** y **Location** para asignarlas como un tipo de dato especial. No estoy seguro si GeoPandas pueda ayudar a ellos.


## [**Finalización**] Entendimiento y planeación
> La ejecución del proyecto se pudó realizar parcialmente a lo planeado, pues hubo muchos aspecto inesperados durante el desarrollo.
**Adicionales ejecutados a lo planeado**
1. Si mas del 65% de una fila eran vacias, se considerarón ruido y se eliminarón.
2. Las fechas que no fueran posibles de estandarizar, como por ejemplo un numero de 5 digitos, se eliminaba la fila completa.
3. La columna de 'Type' se estandarizó a los descriptores 'Provoked', 'Unprovoked' y 'Not specified'
	> La categoria de 'Invalid' fue un criterio de eliminación de la fila. Leyendo a profundidad en los documentos, fuerón casos en los que no se demostraba un **ataque** de un tiburón vivo. Por lo anterior, se entiende que eran casos documentados que no encajaban en el proposito de la base de datos.
4. En la columna 'Activity', los descriptores que no tuvieran la cadena 'ing' eran transformados a 'Not specified'
5. La columna 'Sex' estandarizada a 'F', 'M' y 'Not specified'.
6. Edades estandarizadas al numero y sino existia 'Not specified'. [Funciona con multiples edades]
7. La columna 'Fatal (Y/N)' Estandarizado a 'Y', 'N' y 'Not specified'
8. Las horas se reflejan en una columna dedicada (al igual que el archivo original). Las horas que se pudieran estandarizar, se estandarizaban. Los datos que no se pudieran estandarizar como 'Dusk', 'Afternoon', 'Morning', etc se dejarón en el formato que tenian. Datos vacios y con un minimo de caracteres se estandarizaban a 'Not specified'.
9. Las especies de tiburones se estandarizarón a la palabra antes de la palabra 'Shark'. De no ser posible, 'Not specified'.
10. Se elimina una de las columnas duplicadas con el link del documento.
11. Se añade una columna de indice de lecture adicional a la columna de 'Original order' que no fue alterada.


## Recursos externos:
* [Kaggle.com -> Global Shark Attacks](https://www.kaggle.com/teajay/global-shark-attacks)
