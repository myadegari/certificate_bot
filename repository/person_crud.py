from odmantic import AIOEngine
from bson import ObjectId
from repository.models import Person

class PersonCRUD:
    def __init__(self, engine: AIOEngine):
        self.engine = engine

    async def create(self, data: dict) -> Person:
        person = Person(**data)
        await self.engine.save(person)
        return person

    async def get_by_id(self, person_id: str) -> Person | None:
        return await self.engine.find_one(Person, Person.id == ObjectId(person_id))

    async def get_all(self) -> list[Person]:
        return await self.engine.find(Person)

    async def update(self, person_id: str, data: dict) -> Person | None:
        person = await self.get_by_id(person_id)
        if not person:
            return None
        for key, value in data.items():
            setattr(person, key, value)
        await self.engine.save(person)
        return person

    async def delete(self, person_id: str) -> bool:
        person = await self.get_by_id(person_id)
        if not person:
            return False
        await self.engine.delete(person)
        return True
