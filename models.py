from typing import Type
from fastapi.datastructures import Default
from mongoengine import *
import datetime

from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import *
# from mongoengine import connect, Document, ReferenceField, CASCADEs

class Module(Document):
    
    ServiceId = StringField()
    ParentContainerId = ListField(StringField())
    UsecaseParameter = DictField(default = None)
    ScheduleRuntime = StringField()
    TSCreated = DateTimeField(default=datetime.datetime.utcnow())
    TSModified = DateTimeField()

class ModuleMapping(EmbeddedDocument):
    ScheduledModules = ListField(ReferenceField(Module))
    UncheduledModules = ListField(ReferenceField(Module))

class Camera(Document):
    CameraId = StringField()
    CameraName = StringField()
    Location = StringField()
    Username =  StringField()
    Password =  StringField()
    Link = StringField()
    CameraSource =  StringField()
    CameraStatus =  BooleanField()
    AddedBy =  StringField(default=None)
    RefImage = ListField()
    Modules = EmbeddedDocumentField(ModuleMapping)
    TSCreated = DateTimeField(default=datetime.datetime.utcnow)
    TSModified = DateTimeField()


class ScheduleFlag(Document):
    Status = StringField()

class CameraSource(Document):
    SourceName = StringField()

class CameraHealthCheck(Document):
    HealthCheck = BooleanField()
    HealthCheckInterval = IntField()
    GetAlert = BooleanField()
    UserConsent = BooleanField()

class Taskmeta(Document):
    TaskName = StringField()
    TaskTime = DateTimeField()
    Status = StringField()
    Traceback = StringField()

class ServiceSchedule(Document):
    ScheduleUsecases = ListField()
    SchedulesAIModels = ListField()
    UnscheduleUsecases = ListField()
    UnscheduleAIModels = ListField()

class ServiceCameraMapping(Document):
    ServiceId = StringField()
    ScheduleCameraIds = ListField()
    UnscheduleCameraIds = ListField()  

class ScheduleRunTime(Document):
    OpenTime = StringField()
    CloseTime = StringField()
    HolidaysList = ListField(DateTimeField)

class ReferenceImage(Document):
    CameraId = ReferenceField(Camera)
    ImageType = StringField()
    ImageType = StringField()
    TSCreated = DateTimeField()
    TSModified = DateTimeField()









