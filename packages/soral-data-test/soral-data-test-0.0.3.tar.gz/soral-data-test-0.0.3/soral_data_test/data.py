from xia_fields import StringField
from xia_engine import Document


class TestData(Document):
    _key_fields = ["name"]

    name: str = StringField(description="Name of data")
    description: str = StringField(description="Description of data")
