from odmantic import Model
from datetime import datetime

class Person(Model):
    national_id: str
    student_id: str | None = None
    personnel_id: str | None = None
    full_name: str
    email: str | None = None
    phone_number: str | None = None

class Course(Model):
    course_name: str
    template_path: str
    signer_name: str
    signer_title: str
    sign_image_path: str
    date: datetime
    duration: str

class Certificate(Model):
    person_id: str  # Could be ObjectId, but str if decoupled
    course_id: str
    certificate_number: str
    issue_date: datetime

class Counter(Model):
    key: str  # combination of category + code
    sequence_value: int = 0
