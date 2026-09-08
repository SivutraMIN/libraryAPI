from sqlmodel import SQLModel,create_engine
from . import models # type: ignore

sqlite_file_name = "db.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url,echo=True)


SQLModel.metadata.create_all(engine)