from fastapi import FastAPI
from routers import products,users,basic_auth_users,jwt_auth_users
#from fastapi.staticfiles import StaticFiles

app = FastAPI()
#incluir un router al main
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

#exponer recursos estaticos
#app.mount("/static",StaticFiles(directory="static"),name="static")

#inciciar el servidor : uvicorn main:app --reload
#detener el servidor : 
#documentación de la api con swagger : http://127.0.0.1:8000/docs#/ 
#documentación de la api con redoc : http://127.0.0.1:8000/redoc