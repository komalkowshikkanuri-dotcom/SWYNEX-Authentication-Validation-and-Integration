
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.database import Base, engine
from app import models
from app.routers import users, tasks


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SWYNEX Authentication API",
    description="Backend API with JWT authentication, validation, and protected task management.",
    version="1.0.0"
)


@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": "NOT_FOUND",
                "message": "The requested resource was not found"
            }
        }
    )


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


app.include_router(users.router)
app.include_router(tasks.router)
