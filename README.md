![Portada](https://user-images.githubusercontent.com/64830147/122689610-44ceef00-d224-11eb-95a7-abedde47a2a5.png)
*Este repositorio contiene el segundo proyecto del Bootcamp: Data Analytics de IronHack. El objetivo es la puesta en práctica de todo lo aprendido hasta el momento. Ello incluye limpiar una base de datos, enriquecerla mediante una API o Webscraping y crear un informe con estadísticas y gráficos. El dataset utilizado contiene información sobre los casos de COVID-19, el cuál se encuentra en [Kaggle](https://www.kaggle.com/imdevskp/corona-virus-report).*

# Hipótesis 🤔

![Hipotesis](https://user-images.githubusercontent.com/64830147/122743736-8e045a80-d287-11eb-8d7c-ce2355c72216.png)

Recientemente se han publicado los primeros estudios que sugieren que los sujetos con obesidad o diabetes tienen más disposición a desarrollar una enfermedad más severa por coronavirus. En concreto, los estudios muestran que ambas patologías se consideran factores de riesgo para la hospitalización y el ingreso en UCI así como el desarrollo de consecuencias graves que llevan a la muerte, en caso de enfermedad por COVID-19. 

Partiendo de un conjunto de datos que incluye las estadísticas en materia a el número de afectados por este particular virus, quiero probar la correlación de que en países con un mayor porcentaje de obesidad la tasa de muertes resulta mayor. Del mismo modo que en aquellos en donde dicha cifra es inferior hay una mayor tasa de recuperación y menores casos mortales. 

*Del mismo se procederá a realizar dichas estimaciones con la diabetes y se contrastará con la esperanza de vida de los países seleccionados*

Para realizar el pertinente estudio se han seleccionado 11 países con regímenes y dietas alimentarias muy diversas entre sí: España, Francia, Italia, Grecia, Turquía, China, India, México, Nueva Zelanda y Reino Unido. 

# Índice de contenido 📎
El repositorio incluye:
-	Dataset parciales que contienen por separado la información referente a las estadísticas de covid y porcentajes de obesidad, diabetes y esperanza de vida.
-	Dataset completo (hipótesis_data)
-	4 jupyter notebooks diferenciados en visualización de resultados, tratamiento de la base datos, websrcaping y API (enriquecimiento de datos).
-	Documento py. con las funciones definidas para este proyecto.
-	Carpeta de imágenes.

# Librerías utilizadas 📚

Durante el proyecto se emplearon las siguientes librerías:
-	Pandas
-	Requests
-	Os
-	Json
-	Matplotbit
- Seaborn
- wbdata

 *La documentación oficial se encuentra en el apartado de Links & Recursos*

# Metodología 🔎

Para la limpieza del dataset se emplearon varias técincas:
-	Comprobación de datos duplicados
-	Eliminación de columnas con información irrelevante o no necesaria
-	Selección de la información requeridad (filtrar por país)
-	Renombramiento y estructuración del dataset

Para el enriquecimiento de los datos, se descargaron de diferentes fuentes de información el porcentaje de obesidad y diabetes por país. Los cuales se combinaron en una única tabla para facilitar el ejercicio de visualización.
También se empleo la API de World Bank en materia a la esperanza de vida para contrarrestar la información y los resultados obtenidos.

Con respecto al proceso de visualización se emplearon tanto Seaborn como Matplotlib para la reproducción de los diferentes tipos de gráficos y subtramas que permitieron visualizar las relaciones entre las diferentes columnas. 

# Resultados  ✅
*A continuación se procede al análisis de los resultados obtenidos; para la visualización de más gráficas véase el jupyter notebook 4. Visualization. Además, recalcar que muchos de los factores medidos en las estadísticas del COVID-19 mas allá de las variables estudiadas(obesidad y diabetes) también influyen otras como las medidas tomadas por el Gobierno para hacer frente a la crisis, el acceso a la sanidad, número de población, clima…etc.*

### Obesidad 💟
![Obesidad y muertes]( https://user-images.githubusercontent.com/64830147/122784967-3845a780-d2b3-11eb-80ec-4edae96efff4.png)
Con respecto a la relación entre la obesidad y el número de muertes parece ser que si existe cierta relación ya que en aquellos países donde se produce un mayor número de casos mortales también se da que el índice de obesidad en la población es bastante elevado. Es el caso de Estados Unidos, Reino Unido y México. 

*Cabe destacar que para el caso de Nueva Zelanda y Turquía los cuales presentan un alto grado de obesidad y sin embargo, un número considerablemente inferior de casos mortales. Esto es debido al número de población, así como las medidas favorables y anticipadas tomadas por el Gobierno y el acceso a sanidad que favorecieron una menor propagación y contagio del virus.*

![Obesidad y recuperados]( https://user-images.githubusercontent.com/64830147/122785118-60cda180-d2b3-11eb-84ae-57b34228228a.png)
Desde la perspectiva del porcentaje de recuperados, ocurre lo mismo, a una menor tasa de recuperación mayor grado de obesidad y viceversa como es el caso de China e Italia.

![Esperanza de vida](https://user-images.githubusercontent.com/64830147/122787846-07b33d00-d2b6-11eb-8ce2-83bb36050b17.png)
Si lo contrastamos con el nivel de vida más allá de la pandemia los países con índices de obesidad más bajos son aquellos que presentan una mayor esperanza de vida. 

Ello nos lleva a concluir que la obesidad es una variable que influye de forma negativa para nuestra salud, ya sea como factor de riesgo en casos COVID-19 como en nuestra esperanza de vida. 

### Diabetes 🍬

![Diabetes](https://user-images.githubusercontent.com/64830147/122785761-efdab980-d2b3-11eb-846b-2a108e2ba051.png)

Para el caso de la diabetes sucede lo mismo especialmente en México y Estados Unidos donde los porcentajes de prevalencia en diabetes y casos mortales superan con creces a la tasa de recuperados. Ejemplos como Grecia o Francia cuyo índice de recuperación es alto también se da que hay menos personas con diabetes y menor números de casos mortales. Del mismo modo que si lo contrarrestamos con el nivel de esperanza de vida. 

Concluyendo que también puede existir una relación entre ambas variables, incluyo de mayor grado, con respecto a la obesidad.

### Estudio de correlaciones 🔗

![Correlaciones]( https://user-images.githubusercontent.com/64830147/122785369-9d999880-d2b3-11eb-867c-8b89ba241c9e.png)

En general podemos observar que si existe cierto grado de correlación entre la diabetes (en mayor grado) y la obesidad con las estadísticas del COVID-19.

### Conclusión 🤓
La obesidad y la diabetes pueden considerarse factores de riesgo ante esta enfermedad debido a, en el caso de la primera, por la inflamación que provoca en el organismo el exceso de tejido adiposo que conlleva a una mayor probabilidad de disfunción metabólica y la deficiencia de vitamina D que perjudica al sistema inmune y aumenta el riesgo de padecer infecciones sistemáticas; y en el caso de la segunda, debido a la ausencia de regulación de insulina en la sangre.

Aun así son muchos los estudios requeridos para llegar a una conclusión clara y veraz, aun así, se puede afirmar que las tres patologías se pueden prevenir manteniendo una dieta saludable, actividad física regular, un peso corporal normal y tratando de evitar el consumo de tabaco o alcohol. 

So, let´s be healthy 🫀!

![Conclusión]( https://user-images.githubusercontent.com/64830147/122786736-e736b300-d2b4-11eb-90b3-42b2691a0385.png)



# Links & Recursos 🖇️
- [Kaggle dataset](https://www.kaggle.com/imdevskp/corona-virus-report)
- [Índice de obesidad](https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate)
- [Índice de diabetes](https://www.indexmundi.com/facts/indicators/SH.STA.DIAB.ZS/rankings)
- [World Bank API documentation](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information)
- [Pandas documentation](https://pandas.pydata.org)
- [Requests documentation](https://requests.readthedocs.io/en/master/)
- [Json documentation](https://docs.python.org/3/library/json.html)
- [Matplotbit documentation](https://matplotlib.org)
- [Seaborn documentation](https://seaborn.pydata.org)
- [La obesidad como factor de riesgo en personas con COVID 19](https://www.elsevier.es/es-revista-atencion-primaria-27-articulo-la-obesidad-como-factor-riesgo-S0212656720301657)
- [Por qué los diabéticos son grupo de riesgo frente a la infección Covid-19](https://www.infosalus.com/asistencia/noticia-diabeticos-son-grupo-riesgo-frente-infeccion-covid-19-20200420082733.html)
