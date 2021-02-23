import re
from fastapi.param_functions import Query
from api.utils.aws import uploadfile
from os import access
from fastapi import routing, Depends, Header ,File , UploadFile
import json
import random
import requests
import string
from fastapi.exceptions import HTTPException
from mongoengine.errors import DoesNotExist, ValidationError
import datetime
from mongoengine import Q

from api.utils.jwt import generate_token
from api.utils.auth import authenticate_user
from api.utils.logs import console_logger
from api.db.models import  *
from api.service.sample.serializers import *
from passlib.context import CryptContext
from config import Config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = routing.APIRouter()

@router.post("/login")
async def end_point_for_login():
    try:
        return 'success'
    except Exception as e:
        return {
            'error_message' : str(e)
        }