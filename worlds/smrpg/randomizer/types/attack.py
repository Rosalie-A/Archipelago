from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttack as EnemyAttackBase
class EnemyAttack(EnemyAttackBase):
    _remake_name: str | None = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._name
