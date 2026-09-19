from pydantic import BaseModel


class AnalyzeEmail(BaseModel):
    category: str
    summary: str
    priority: str
    action: str