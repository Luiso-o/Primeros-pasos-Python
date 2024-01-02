from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"], #documentacion swagger
                    responses={404: {"message" : "No encontrado"}})

products_list = ["Producto1","Producto2","Producto3","Producto4","Producto5"]

@router.get("/")
async def products():
    return products_list