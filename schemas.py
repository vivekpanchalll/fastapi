from pydantic import BaseModel, Field,ConfigDict,FieldValidationInfo

class PostBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=3, max_length=1000)
    author: str = Field(..., min_length=3, max_length=100)

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass    

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: str