## **Ramas:**
=========================================================

- main -> Codigo totalmente funcional
- develop -> Codigo fusionado y bajo prueba antes de pasar a main
- feature/<nombre> -> Espacio de trabajo asignado a cada uno

## **Organizacion de archivos:**
=========================================================

- Repositorios -> Solo archivos dao
- Modelos -> Entidades de la base de datos
- BaseDeDatos -> Conexion, Inicializacion de la DB y el sql de la base
- Servicios -> Logica de negocio para acceso a datos
- UI -> Todo relacionado a FrontEnd
- Controladores -> Capa de comunicacion entre FrontEnd y capa de Servicios
- Reportes -> Datos formateados y listos para ser mostrados en el FrontEnd
- Assets -> Recursos necesarios para el FrontEnd

## **Comandos importantes:**
========================================================

Clonar (descargar) el repositorio (Solo la primera vez para descargar todo)
- git clone "https://github.com/CodenameChronos/project-sco.git" 

Cambiar a tu rama o espacio de trabajo (reemplazar nombre con tu nombre con inicial mayuscula y sin tilde en el caso de Maria)
- git checkout feature/nombre

Agregar o guardar los cambios de todos los archivos a tu rama
- git add .

Confirmar los cambios guardados (reemplazara mensaje por una breve descripcion del cambio, agregar antes del mensaje fix: para correccion de errores, feat: para agregados de avances o refactor: para cambios que no alteraron logica previa)

-git commit -m "mensaje"

Subir los cambios al repositorio github de la rama o espacio de trabajo en que estas actualmente
- git push

Descargar los cambios de la rama de la persona especificada
- git pull origin feature/nombre

## **Indicaciones generales:**
=============================================================

- Todos los archivos de logica de negocio iran en carpeta de Servicios, esto incluye las clases que realizan los calculos financieros esenciales del sistema, por orden y nomenclatura, usar solo minusculas, sin tildes, separando con "_" cuando se requiera un espaciado y agregar la palabra service al final, esto con el fin de estandarizar los nombre y no tener que revisar todo el rato

- Al usar git checkout seguido del nombre de la rama de otra persona pueden acceder a su rama de github (no la local de esa persona) y ayudar de manera remota con su trabajo

- Si alguien que no seas tu altera tu rama, recuerda hacer git pull origin feature/tunombre para descargar los cambios que se hayan hecho

- Si accedes a la rama de alguien mas, recuerda regresar a la tuya con git checkout feature/tunombre antes de seguir trabajando en lo tuyo

- Realizar commits frecuentemente, con el fin de tener un historial de trabajo con puntos de guardado menos saturados y una mayor facilidad para leer dicho historial