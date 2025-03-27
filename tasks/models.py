import ormar
from database import base_ormar_config


class Task(ormar.Model):
    ormar_config = base_ormar_config.copy(tablename="tasks")    

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(nullable=False, max_length=100)
    description: str = ormar.String(nullable=False, max_length=1000)
