from database.database import get_session
from database.models import Users
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.api.airport import airport_router
from src.api.auth import auth_router
from src.api.booking import booking_router
from src.api.country import country_router
from src.api.flight import flight_router
from src.api.office import office_router
from src.api.user import user_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth")
api_router.include_router(user_router, prefix="/user")
api_router.include_router(office_router, prefix="/office")
api_router.include_router(flight_router, prefix="/flight")
api_router.include_router(airport_router, prefix="/airport")
api_router.include_router(booking_router, prefix="/booking")
api_router.include_router(country_router, prefix="/country")


@api_router.get("/serverStatus")
async def server_status(session: AsyncSession = Depends(get_session)):
    try:
        await session.execute(select(Users))
        return {"detail": "server and database are working!"}
    except Exception as e:
        print(e)
        return {"detail": "connection to the database is corrupted"}
