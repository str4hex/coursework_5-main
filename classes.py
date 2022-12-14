from dataclasses import dataclass
from skills import FuryPunch, Skill, HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill



WarriorClass = UnitClass(
    name="Орк",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch(),
)

ThiefClass = UnitClass(
    name="Гном",
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot(),
)


# Экземпляр какие есть персонажи
unit_classes = {ThiefClass.name: ThiefClass, WarriorClass.name: WarriorClass}
