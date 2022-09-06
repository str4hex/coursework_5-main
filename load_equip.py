import json


class LoadEquip:
    res_all = {}

    def load_json(self) -> str:
        with open('data/equipment.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    def load_weapons(self) -> None:
        pars = lambda: [x['name'] for x in self.load_json()['weapons']]
        result = self.res_all.update({'weapons': pars()})


    def load_armors(self) -> None:
        pars = lambda: [x['name'] for x in self.load_json()['armors']]
        result = self.res_all.update({'armors': pars()})

    def test(self):
        res = 
        return res()


x = LoadEquip()
x.test()
print(x.test())