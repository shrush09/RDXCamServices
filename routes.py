import re
import pymongo
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import json
import mongoengine
from models import *
from  serializers import *
from pymongo import MongoClient
from pymongo import ReturnDocument


mongoengine.connect(db="RDXCameraServices", host="localhost", port=27017)
mongo_client = MongoClient('mongodb://localhost:27017')

db = mongo_client["RDXCameraServices"]


app = FastAPI()


@app.post("/camera/", response_model=CameraInputPostOut)
async def create_user(camera_user: CameraInputPostIn ):
    data = camera_user.dict()
    Camera(**data).save()
    return data


def updateModuleList(runtime, cam_data, Module_profile):
    scheduled = []
    unscheduled = []
    
    # Check if Modules table is empty
    if cam_data.Modules is None:
        # append Objectid of that Module in "scheduled" list
        scheduled.append(Module_profile.id)
        Cam_map = ModuleMapping(**{"ScheduledModules" : scheduled, "UncheduledModules": unscheduled})
        cam_data.Modules =  Cam_map
       
    else:

        scheduled = (cam_data.Modules.ScheduledModules).copy()
        unscheduled = (cam_data.Modules.UncheduledModules).copy()

        if runtime == "Scheduled":
            scheduled.append(Module_profile.id),
        else:
            unscheduled.append(Module_profile.id)

        Cam_map = ModuleMapping(**{"ScheduledModules" : scheduled, "UncheduledModules": unscheduled})

        cam_data.Modules =  Cam_map

    return cam_data


@app.post("/Module/")
async def camera_module_list(payload:ModuleList, camera_id : str):
 
    # Validation To check if camera id is present or not
    cam_data = Camera.objects(CameraId=camera_id).get()
    datamod = {}
    data = payload.dict()

    for mods in cam_data.Modules.ScheduledModules:
        # print(mods.id)
     
        datamod[mods.id] = {
            "Id": mods.id,
            "ServiceId" : mods.ServiceId
        }
        
        datamod[mods.id]["ParentContainerId"] = mods.ParentContainerId

    # print(datamod)
    for payload.ServiceId in data["ModuleData"]:
        
        # print(module)
        
        if module["ServiceId"] in datamod[mods.id]["ServiceId"]:
            print("OKKKKKKK")

            Module_profile = Module(
                    ParentContainerId = module["ParentContainerId"],
                    ScheduleRuntime = payload.ScheduleRuntime,
                    ServiceId = module["ServiceId"]
                ).save()
        
        
            
            
        # print(Module_profile.id)


            camdata_object = updateModuleList(payload.ScheduleRuntime, cam_data, Module_profile)

            camdata_object.save()
    
                
      
    return "Success"



"""
# print(ModulesPresent)
    # for mod in ModulesPresent:
    #     print(mod)
    # iterate in payload list and assign the user input and save in Module table
    for module in data["ModuleData"]:
        # print(module)
        
        # collection.replace_one({'Student': student, 'Date': date}, record, upsert=True)
        # mycol = db["user"]

    # print(db.permissions.find_one_and_update({
    #     "user_id":user_profile.id
    # },
    # {
    #     "$set":{
    #         "permission_id":permission_type_profile.id
    #     }
    # },
    # return_document = ReturnDocument.AFTER
    # ))
        # Module_profile = db.module.update_one({
        #     "ParentContainerId" : module["ParentContainerId"],
        #     "ScheduleRuntime" : payload.ScheduleRuntime,
        #     "ServiceId" : module["ServiceId"]
        # },
        # upsert = True)
        # Module_profile.save()
        Module_profile = Module(
            ParentContainerId = module["ParentContainerId"],
            ScheduleRuntime = payload.ScheduleRuntime,
            ServiceId = module["ServiceId"]
        ).save()

        # print(Module_profile.id)


        camdata_object = updateModuleList(payload.ScheduleRuntime, cam_data, Module_profile)

        camdata_object.save()
            
            """
