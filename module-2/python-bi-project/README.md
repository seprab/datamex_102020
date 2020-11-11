> Hola Mayumi, a continuación encontrarás dos partes del README, la primera nombrada ***'¿Donde Ubicar Mi Empresa?'*** y la segunda ***'Resolución del Problema'***. 
1. La primera sección la destine a descubrir que tipo de empresa queria posicionar en el mundo y me hice a diferentes ideas de como hacerlo.
2. La segunda sección la escribo despues de finalizar el proyecto, dado que los resultados esperados durante el proyecto no fuerón los mejores, tuve que improvisar hasta llegar al resultado.

[La ruta al código](https://github.com/seprab/datamex_102020/blob/w4_m2_d5_pythonBiProject/module-2/python-bi-project/MongoDBFiltering.ipynb)


# ¿Donde Ubicar Mi Empresa?

Para dar inicio al proyecto creo que lo primero debo definir es: ¿Cual es mi empresa?
> En dado caso yo quiera crear una empresa, esta sería de innovación/tecnologia. Dicho esto, creo que este tipo de empresas no se crean eligiendo un lugar fisico en el mundo, por mas que las oficinas se rodeen de gimnasios, starbucks, bubble tea o lo que sea... el verdadero beneficio que buscan los empleados de tecnologia es trabajar de manera remota en su entorno. Por lo anterior, planteare diferentes tipos de empresas con las que podría trabajar el proyecto.

## Posibles empresas
1. **Bubble Tea** Es una bebida que ha adquirido mucha popularidad en los ultimos años y se encuentra presente en todas partes del mundo. Posiblemente por lo mismo, es una idea a descartar.
2. **Pokemón Cafe** He visto que en Japón existen tiendas temáticas, entre esas de pokemón. En dicho país estos lugares tienen mucho exito, reservas ocupadas por tiempos prolongados. Los lugares, adornos, comidas, bebidas,... todo esta relacionado a la tematica
3.  **Karts** Pero no solo de mini-karts, sino tambien de motos pequeñas. Se que en Bogotá, Colombia en el parqueadero de algún centro comercial hay karts donde tambien se pueden usar motos pequeñas para competir.
4.  **Parque de diversiones** Tematico a algúna franquicia de pelicula o videojuegos. Creo que no.
5.  **Tienda de regalos para hombre** Generalmente las tiendas de compras son orientadas en su mayoria a las mujeres. [Semilla de la idea](https://crearmiempresa.es/30-ideas-para-montar-negocios-con-futuro.html)
6.  **Talleres 24/7 de motos y ciclas** Me imagino un lugar con espacio para 50 motos/ciclas, cada estación individual con dispocisión de toda herramienta necesaria para realizar ajustes, calibración, mantenimientos, lavado y un cobro por hora. [Semilla de la idea](https://crearmiempresa.es/30-ideas-para-montar-negocios-con-futuro.html)


## (Motor) Ciclismo 24/7
> Empresa seleccionada de las opciones que expuse anteriormente porque me parece que es algo que no existe y que podría funcionar supremamente bien siempre y cuando se cumplan los criterios de selección.
### Criterios de selección
- Debe ubicarse en un lugar con mucho trafico, concentración 'trancones' infinitos.
- Debe ser una de las ciudades con mas motos en el mundo, pero tambien con población y la capacidad para gastar en ello.
- Debe ser una de las ciudades entre el top del mundo donde las personas use cicla para movilizarce.
-  Facil acceso (?)
- Rodeado de muchas oficinas (?)
- Elegir lugares 

## ¿Que voy a hacer?
> no se.

1. Hemos recibido una base de datos .JSON que podemos leer con MongoDB. De primera mano, la base de datos consta de 18801 documentos, cada documento representando una empresa. Los datos que contiene cada empresa son:

Celdas | Celdas | Celdas | Celdas 
------------ | ------------- | ------------- | ------------- 
_id | name | permalink | crunchbase_url
homepage_url | blog_url | blog_feed_url | twitter_username
category_code | number_of_employees | founded_year | founded_month
founded_day | deadpooled_year | tag_list | alias_list
email_address | phone_number | description | created_at
updated_at | overview | image | products | relationships
competitions | providerships | total_money_raised | funding_rounds
investments | acquisition | acquisitions | offices
milestones | video_embeds | screenshots | external_links
partners | | |
2. De todo lo anterior, que datos me podria interesar?
	- **1_id** Siempre necesario
	- **2.name** Para conocer la empresa filtrada
	- **9.category_code** Es posible que si encuentro alguna relación a la idea de empresa, 
	- **15.tag_list** Posiblemente investigar tags relacionados a la empresa del proyecto
	- **19.description** El mismo objetivo del punto anterior
	- **26.competitions** Si encuentro alguna empresa, ¿esta tiene competencia?
	- **33.offices** Para conocer en que lugar del mundo se podría encontrar
	- **38.parters** Que alianzas tiene con otras marcas para impulsar su mercado?
3. Existen distintas opciones posibles dados los resultados:
- *Opción 1:* Si encuentro empresas que encajen mi busqueda, debería tratar de identificar los criterios de selección de ubicación por los cuales abrierón en determinados lugares.
- *Opción 2:* En caso que la base de datos no me proporcione la información que estoy buscando, puedo hacer uso de la api de google para realizar dicha investigación.
- Opción 3: Y menos deseada es realizar la busqueda a mano, pero entonces no aporia nada al proyecto (?) 
7. Dados los:
	1. Criterios de selección propios
	2. Criterios de selección de competencias
	3. Oficinas (address) de competencias
**Efectuar la estrategia de selección**



# Resolución del Problema

Durante el desarrollo del reto me enfrente a diferentes obstaculos que no permitierón encajar mi idea de empresa para el desarrollo del proyecto.

1- Al inicio del proyecto mi empresa era un lugar donde motociclistas y ciclistas del día a día podrían acercarse para realizar mantenimiento a sus herramientas de movilidad. La idea es que el mismo dueño del vehiculo haga sus mantenimientos y aseo haciendo uso de las herramientas disponibles en las instalaciones de la empresa.
2- ***¡Ho sorpresa!*** Implemente las tecnicas de filtrado necesario con MongoDB, pero me di cuenta que la base de datos estaba mayormente orientada a empresas de tecnologia.
	- Social Media
	- Video Juegos
	- y mas...
> El porcentaje de empresas categorizadas en el ambito de 'Movilidad' era extremadamente pequeño. Me parece que llegue al punto de filtrar 19 empresas relacionadas.

3- Al encontrar el pequeño porcentaje de empresas de movilidad, me parecia bien. Por lo anterior, tomé la iniciativa de investigar cada una de esas empresas filtradas.

4- ***¡Ho sorpresa!*** esas empresas de movilidad eran tipo 'Tesla', compra-venta de usados, construcción de partes mecanicas, etc.... Nada que ver con mi idea.

*Para este punto realice una pausa porque descubrí que tenia la completa libertad de elegir cualquier parte del mundo ***PERO*** sin hacer uso de la BDs.*

> Tomé la decisión de realizar web scrapping para seleccionar los paises que mas usan bicicletas *y* motos, encontrando a Colombia e Italia en estas coincidencias. Posteriormente, Oscar nos aclaró que la idea del proyecto es hacer uso de MongoDB. Y por esta razón, retomé el proyecto con la misma BDs pero con nuevos criterios de selección.


### Nuevos Criterios de Selección
- La ciudad con mas número de empleados en el mundo dada la base de datos.

***No más.*** En realidad queria descubrir en que parte del mundo se concentraba la mayor parte de empleados, teniendo en consideración todas las empresas de la base de datos.
Si habian empresas con varias oficinas, yo realizaba la división en partes iguales del número de empleados por cada oficina.

1. Posterior, a realizar la agrupación y suma de empleados de todas las empresas por ciudad, descubrí el siguiente TOP:

Ciudad | Número Empleados  
------------ | ------------- 
Tokyo | 514178
San Jose | 499412
Munich |405426
Armonk |388000
Aichi | 320000
Falls Church | 272940
San Diego | 240676
New York | 199233
Pleasanton | 191019
Seoul |	177919

>En el código muestro el top 30 de ciudades

2. Seguido, realicé web scrapping del TOP 30 de ciudades del múndo con mas ciclistas. No encontre el mismo top con motos.
3. Encontré las ciudades coincidentes entre el TOP número de empleados y el TOP con mas ciclistas. El resultado es ***Montreal***.

## Conclusiones

1. Las empresas en la base de datos a pesar de ser grande, no recoge gran variedad de tipos de empresas ni de todos los paises del mundo.
2. El resultado hayado contradice mis criterios antes de iniciar el proyecto. En Montreal caé nieve 1/3 del año, lo cual invalida la selección.
3. Montreal no hace parte de los paises con mas motociclistas ***Y*** ciclistas del mundo. 
