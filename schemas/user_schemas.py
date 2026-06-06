from pydantic import BaseModel
class Usercreate(BaseModel):
    name: str
    email: str
class userupdate(Usercreate):
   id: int
class userresponse(userupdate):
    pass