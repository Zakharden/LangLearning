import json


class Hedgehog:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.get_info()
        self.check()

    def get_info(self):
        data = {"name": self.name,
                "race": self.race}

        json_data = json.dumps(data, ensure_ascii=False)
        print(json_data)

    def check(self):
        if 'еж' in self.race or 'ёж' in self.race:
            print(f'{self.name} — коренной житель!')
        else:
            print(f'{self.name} — приезжий!')

while True:
    datas = input('Введите своё имя и вид: ').split(', ')
    person = Hedgehog(datas[0], datas[1])
