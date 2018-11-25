import string
import datetime

from dataclasses import dataclass

@dataclass
class Perfil:
    academic_register: str
    complete_name: str
    social_name: str
    genre: str
    social_genre: str
    birth_date: datetime.datetime
    nacionality: str
    birth_state: str
    birth_city: str
    birth_country: str
    father_name: str
    mother_name: str
    cep: str
    address: str
    address_number: int
    complement: str
    neighborhood: str
    city: str
    state: str
    telephone: str
    lattes: str
    email: str
    cpf: str
    rg: str
    document_agent: str
    document_state: str
    election_title_zone: str
    election_title_number: str
    number: str
    category: str
    agente: str
    date: str
    degree: int
    type: str
    year: int
    instituition: str
    course: str
    instituition_country: str
    instituition_state: str
    institution_city: str
    first_name: str = ""

    def __post_init__(self):
        if type(self.address_number) is str:
            self.address_number = int(self.address_number)

        if type(self.degree) is str:
            self.degree = int(self.degree)

        if type(self.year) is str:
            year = self.year.replace(",", "")
            year = int(year)

            self.year = year

        if type(self.telephone) is str:
            ddd = self.telephone[0:2]
            telephone = self.telephone[2:].strip()

            self.telephone = ddd + telephone

        cap_word_fields = [
            "birth_city",
            "birth_state",
            "birth_country",
            "city",
            "complement",
            "complete_name",
            "course",
            "document_state",
            "father_name",
            "instituition",
            "institution_city",
            "instituition_state",
            "instituition_country",
            "mother_name",
            "nacionality",
            "neighborhood",
            "neighborhood"
        ]

        for cap_word_field in cap_word_fields:
            setattr(
                self, cap_word_field, string.capwords(
                    getattr(self, cap_word_field)
                )
            )

        self.first_name = self.complete_name.partition(' ')[0]
        self.birth_date = datetime.datetime.strptime(self.birth_date, '%d/%m/%Y')
