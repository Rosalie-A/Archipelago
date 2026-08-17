from ..ItemNames import ItemNames


class RequirementItemMetaclass(type):
    name: ItemNames

    def __repr__(self):
        return self.name.value

class RequirementItem(metaclass=RequirementItemMetaclass):
    name: ItemNames

    def __repr__(self):
        return self.name.value

class RequirementItemGroup(RequirementItem):
    members: list[RequirementItemMetaclass]

    def __repr__(self):
        return ", ".join([member.value for member in self.members])