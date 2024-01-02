#Creacion de un CRUD con Python y FastAPI
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#Instanciamos FastAPI 
router = APIRouter(prefix="/users",
                   tags=["users"], #documentacion swagger
                    responses={404: {"message" : "No encontrado"}})

#Creamos una entidad apoyandonos de BaseModel
class User(BaseModel):
    id: int 
    name: str 
    surname: str
    url : str
    age : int

#simular una base de datos  
users_list = [User(id=1,name="Luis",surname="Trujillo",url="https://github.com/Luiso-o",age=32),
         User(id=2,name="Mario",surname="Jimenez",url="https://mariosite/ejemplo",age=33),
         User(id=3,name="Karla",surname="Perez",url="https://karlasite/ejemplo",age=30)]

#creamos la peticion al servidor GET
@router.get("/")
async def getUsers(): 
    return users_list

#buscar por id usando path
@router.get("/{id}")
async def getUsersById(id:int): 
    return search_user(id)
#pedicion ej: http://127.0.0.1:8000/users/1
    
#buscar por id usando query
@router.get("/usersquery/")
async def getUsersById(id:int): 
    return search_user(id)
    #pedicion ej: http://127.0.0.1:8000/usersquery/?id=1

#POST
@router.post("/user/",response_model=User, status_code = 201)
async def createUser(user : User):

  #http status code
  if type(search_user(user.id)) == User:
    raise HTTPException(status_code = 404, detail = "El usuario ya existe")
 
  users_list.append(user)
  return user


#PUT
@router.put("/update/")
async def updateUser(user:User):

  found = False

  for index, saved_user in enumerate(users_list):
   if saved_user.id == user.id:
      users_list[index] = user
      found = True
  
  if not found:
      return {"error: no se ha actualizado el usuario"}
  else:
     return user
    

#Delete
@router.delete("/delete/{id}")
async def deleteUser(id: int):

  found = False

  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
      del users_list[index]
      found = True

  if not found:
    return {"error: no se ha eliminado el usuario"} 
  
  return {"message": "Usuario eliminado correctamente"}

   
#funcion para buscar un usuario
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
       return list(users)[0]
    except:
      return {"error: no se ha encontrado el usuario"}

