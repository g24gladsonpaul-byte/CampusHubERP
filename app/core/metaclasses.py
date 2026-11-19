
from datetime import datetime


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        original_init = attrs.get("__init__")

        def __init__(self, *args, **kwargs):
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            if original_init:
                original_init(self, *args, **kwargs)

        attrs["__init__"] = __init__

        return super().__new__(cls, name, bases, attrs)
