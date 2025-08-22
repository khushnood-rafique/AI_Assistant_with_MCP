import re
from pydantic import BaseModel, Field, field_validator

class DateTimeModel(BaseModel):
    date: str = Field(description="Formatted date", pattern= r'^\d{2}-\d{2}\d{4} \d{2}:\d{2}$')

    @field_validator('date')
    def validate_date(cls, value):
        if not re.match(r'^\d{2}-\d{2}\d{4} \d{2}:\d{2}$', value):
            raise ValueError("Date must be in DD-MM-YYYY HH:MM format")
        return value