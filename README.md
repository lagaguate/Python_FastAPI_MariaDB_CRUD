# Python_FastAPI_MariaDB_CRUD
## Configurar Entorno
1. Activar Docker con MariaDB (mysql)
```sh
 sudo docker start mysql
```

## Intalar en el proyecto.
1. Iniciarlizar proyecton con Git
```sh
 git init
```
2. En Conda uvicorn
```sh
  conda activate fast-api
```
3. En Conda FastAPI
```sh
  uvicorn main:app --reload
```
4. Instalar sqlalchemy en Conda
```sh
 conda install -c anaconda sqlalchemy
```
5. Instalar pymysql en conda -n fast-api
```sh
conda install -c anaconda pymysql
6. Instalar criptography en conda -n fast-api
```sh
conda install -c anaconda cryptography -n fast-api
```
7. Instalar criptography en conda -n fast-api
```sh
conda install -c conda-forge werkzeug -n fast-api
```


# Generar un archivo de requerimienots

- ip freeze >requirements.txt