### Main application script ###
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect 
 
from api.service.sample.routes import router as sample_router
from api.utils.responses import responses

app = FastAPI()

connect(db="toogle", username="admin", password="tgroot123", host="mongo", authentication_source="admin")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(
        sample_router,
        prefix="/sample",
        tags=["Sample"],
        responses=responses
    )
