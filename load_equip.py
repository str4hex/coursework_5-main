import json


class LoadEquip:
    res_all = {}

    def _load_json(self) -> str:
        with open('data/equipment.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    def _load_weapons(self) -> None:
        pars = lambda: [x['name'] for x in self._load_json()['weapons']]
        result = self.res_all.update({'weapons': pars()})

    def _load_armors(self) -> None:
        pars = lambda: [x['name'] for x in self._load_json()['armors']]
        result = self.res_all.update({'armors': pars()})

    def _load_class(self):
         self.res_all.update({"classes": ["Воин", "Вор","Орк","Эльф","Гном"]})

    @property
    def load(self):
        self._load_class()
        self._load_armors()
        self._load_weapons()
        return self.res_all

