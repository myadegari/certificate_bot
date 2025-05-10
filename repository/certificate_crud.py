from odmantic import AIOEngine
from bson import ObjectId
from repository.models import Certificate
from utils.certificate_number_generator import CertificateNumberGenerator
from datetime import datetime

class CertificateCRUD:
    def __init__(self, engine: AIOEngine):
        self.engine = engine
        self.generator = CertificateNumberGenerator(engine)

    async def create(self, data: dict) -> Certificate:
        if "certificate_number" not in data:
            category = data.get("category", "الف")  # Default category
            code = data.get("code", "000")         # Default course code
            data["certificate_number"] = await self.generator.generate(category, code)

        if "issue_date" not in data:
            data["issue_date"] = datetime.now()

        cert = Certificate(**data)
        await self.engine.save(cert)
        return cert

    async def get_by_id(self, cert_id: str) -> Certificate | None:
        return await self.engine.find_one(Certificate, Certificate.id == ObjectId(cert_id))

    async def get_all(self) -> list[Certificate]:
        return await self.engine.find(Certificate)

    async def get_by_certificate_number(self, cert_number: str) -> Certificate | None:
        return await self.engine.find_one(Certificate, Certificate.certificate_number == cert_number)

    async def get_by_person_identifier(self, identifier: str) -> list[Certificate]:
        return await self.engine.find(Certificate, Certificate.person_identifier == identifier)

    async def update(self, cert_id: str, data: dict) -> Certificate | None:
        cert = await self.get_by_id(cert_id)
        if not cert:
            return None
        for key, value in data.items():
            setattr(cert, key, value)
        await self.engine.save(cert)
        return cert

    async def delete(self, cert_id: str) -> bool:
        cert = await self.get_by_id(cert_id)
        if not cert:
            return False
        await self.engine.delete(cert)
        return True
