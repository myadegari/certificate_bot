from odmantic import AIOEngine
from repository.models import Certificate

class CertificateNumberGenerator:
    def __init__(self, engine: AIOEngine):
        self.engine = engine

    async def generate(self, category: str, course_code: str) -> str:
        # Find all certificates with the same category and code
        prefix = f"{category}/{course_code}"
        certs = await self.engine.find(
            Certificate,
            Certificate.certificate_number.regex(f"^\\d+/{prefix}$")
        )

        # Extract max numeric part
        max_number = 0
        for cert in certs:
            try:
                number_part = int(cert.certificate_number.split("/")[0])
                max_number = max(max_number, number_part)
            except (IndexError, ValueError):
                continue

        next_number = max_number + 1
        return f"{next_number:03}/{category}/{course_code}"
