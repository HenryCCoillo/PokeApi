<div align="center">
<h1 style="text-align: center;">Proyecto POCKEAPI - Ruta B1</h1>
</div>


# Despliegue en AWS

  ### Usuario Prueba
```bash
henry@123.com
```
  
### Password
```
12345678
```
  
  ![image](https://user-images.githubusercontent.com/86704638/218283415-63e1ad0d-fa82-4275-899c-240559024d2c.png)


  http://52.201.180.165/                  Frontend
  
  http://52.201.180.165:8000/             Backend
  
  http://52.201.180.165:8000/login/       Login User
 
  http://52.201.180.165:8000/signup/      Register User
  
  http://52.201.180.165:8000/swagger/     Swagger
  
  http://52.201.180.165:8000/pokeapi/v3/  Lista Pokemon
  
  




# Proyecto Pokemon Api Frontend (Complementario)

https://github.com/HenryCCoillo/PokeApi-Frontend


Integrantes:

- 👨‍💻 Henry Ccoillo
- 👨‍💻 Starky Medina Caldas
- 👨‍💻 Jhohan Jancco Chara

<hr>

## Descripcíon
- Es un Proyecto de DjangoRestFramework que se encarga de listar Pokemon y visualizar habilidadades
- Tiene un login y signup (JWT) http://127.0.0.1:8000/login/ y http://127.0.0.1:8000/signup/
- Es Proyecto tiene que estar Autenticado, obtener los datos del pokemon
- La lista para obtener una Paginacion de 10 Pokemon
- Para obtener la lista de Pokemon esta en http://127.0.0.1:8000/pokeapi/v3/
- Para obtener los datos del Pokemon esta en http://127.0.0.1:8000/pokeapi/v3/1/
- El Proyecto tambien esta diseñado para que puedas Ingresar el nombre del Pokemon http://127.0.0.1:8000/pokeapi/v3/bulbasaur/

## Requisitos
- Python 3.10

## Instalacion
#### Crear entorno Virtual
```bash
python3 -m venv env
```
#### Activar el entorno Virtual (Windows)
```bash
env\Scripts\activate.bat
```
#### Instalar los Requisitos
```bash
pip install -r requirements.txt
```

#### Iniciar Proyecto
```bash
python manage.py runserver
```
<br>

- ### Todas las ruta de Swagger en http://127.0.0.1:8000/swagger/
![image](https://user-images.githubusercontent.com/86704638/217305994-0025e7e8-4b70-41f1-975d-c5572544496f.png)


- ### Para Usar Swagger tiene que "DESCOMENTAR" "authentication_classes = [SessionAuthentication, BasicAuthentication]", la ruta esta en /pokeapi/api.py

<br>

![image](https://user-images.githubusercontent.com/86704638/217306322-9bc230db-7859-47e3-a1f1-d0966c5cfa5e.png)
