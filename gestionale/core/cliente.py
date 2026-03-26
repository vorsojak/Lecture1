from dataclasses import dataclass


@dataclass
class ClienteRecord:
    name: str
    mail: str
    categoria: str

    def __hash__(self):
        return hash(self.mail)

    def __eq__(self, other):
            return self.mail == other.mail

    def __str__(self):
        return f"{self.name} -- {self.mail}, {self.categoria}"