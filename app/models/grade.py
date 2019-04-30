from app.models.discipline import Discipline


class Grade:
    def __init__(self, disciplines):
        print(disciplines)
        self.disciplines = [
            Discipline(*[field for field in discipline]).__dict__
            for discipline in disciplines
        ]
