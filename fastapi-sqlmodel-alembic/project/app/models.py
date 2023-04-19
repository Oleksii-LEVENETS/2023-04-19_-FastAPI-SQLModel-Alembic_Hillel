from typing import Optional

from sqlmodel import Field, SQLModel


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


# class SongBase(SQLModel):
#     name: str
#     artist: str


class Song(SongBase, table=True):
    id: int = Field(default=None, primary_key=True)  # noqa: A003


class SongCreate(SongBase):
    pass
