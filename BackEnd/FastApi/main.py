from fastapi import FastAPI
from routers import products
from routers import users


app = FastAPI()
#incluir un router al main
app.include_router(products.router)
app.include_router(users.router)


#inciciar el servidor : uvicorn main:app --reload
#detener el servidor : 
#documentación de la api con swagger : http://127.0.0.1:8000/docs#/ 
#documentación de la api con redoc : http://127.0.0.1:8000/redoc