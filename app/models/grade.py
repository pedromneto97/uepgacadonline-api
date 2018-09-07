from app.models.discipline import Discipline

import json


class Grade:
    def __init__(self, disciplines):
        self.disciplines = [
            Discipline(*[field for field in discipline]).__dict__
            for discipline in disciplines
        ]

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
