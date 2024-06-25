from pydantic import BaseModel
from typing import List

class PackInfo(BaseModel):
    name: str
    versions: List[str]
    timestamp: str