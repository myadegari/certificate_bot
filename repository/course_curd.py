from odmantic import AIOEngine
from bson import ObjectId
from repository.models import Course

class CourseCRUD:
    def __init__(self, engine: AIOEngine):
        self.engine = engine

    async def create(self, data: dict) -> Course:
        course = Course(**data)
        await self.engine.save(course)
        return course

    async def get_by_id(self, course_id: str) -> Course | None:
        return await self.engine.find_one(Course, Course.id == ObjectId(course_id))

    async def get_all(self) -> list[Course]:
        return await self.engine.find(Course)

    async def update(self, course_id: str, data: dict) -> Course | None:
        course = await self.get_by_id(course_id)
        if not course:
            return None
        for key, value in data.items():
            setattr(course, key, value)
        await self.engine.save(course)
        return course

    async def delete(self, course_id: str) -> bool:
        course = await self.get_by_id(course_id)
        if not course:
            return False
        await self.engine.delete(course)
        return True
