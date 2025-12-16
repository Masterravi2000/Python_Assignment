from pydantic import BaseModel, Field

class EntityWithAttr(BaseModel):
    entity: str = Field(description="Exact entity name")
    attr_type: str = Field(description="Semantic type like Crop, Drug, Process")