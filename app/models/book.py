from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    book_id: str = Field(..., alias="_id") # Precisa sem _id porque os dados virão do MongoDB que por sua vez retorna _id.
    title: str
    subtitle: str
    authors: list[str]
    isbn: str
    category: str

class Config:
    populate_by_name = True