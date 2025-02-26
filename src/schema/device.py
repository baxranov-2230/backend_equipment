from pydantic import BaseModel


class DeviceData(BaseModel):
    name: str
    model: str
    seria_num: str
    status: str
    user_id: int

class DeviceCreateRequest(DeviceData):
    class Config:
        from_attributes = True


class DeviceCreateResponse(DeviceData):
    id: int
    class Config:
        from_attributes = True