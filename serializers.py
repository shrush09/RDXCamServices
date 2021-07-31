from typing import Dict, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from models import *
import datetime


class CameraInputPostIn(BaseModel):
    CameraId : str
    CameraName : str
    Location : str
    Username :  str
    Password :  str
    Link : str
    CameraSource :  str
    CameraStatus :  bool
    RefImage : list


class CameraInputPostOut(BaseModel):
    CameraId: str

# Take the input in list, 
class ModuleInput(BaseModel):
    ParentContainerId : List[str]
    ServiceId : str
    
class ModuleList(BaseModel):
    ScheduleRuntime : str
    ModuleData : List[ModuleInput]
 