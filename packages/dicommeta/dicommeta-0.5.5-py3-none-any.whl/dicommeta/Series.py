from typing import Dict, Iterable

from attr import define, field
from attrs import asdict

from dicommeta import Instance


@define(kw_only=True, slots=True, order=True, frozen=True)
class Series:
    seriesUID: str = field(factory=str)
    instance_dict: Dict[str, Instance] = field(factory=dict)

    def add_instance(self, instance: Instance):
        if instance.SOPinstanceUID not in self.instance_dict.keys():
            self.instance_dict[instance.SOPinstanceUID] = instance

    def get_instance(self, instance_uid: Instance) -> Instance:
        return self.instance_dict[instance_uid]

    def get_dict(self):
        return asdict(self)

    def get_iter(self) -> Iterable:
        return iter(asdict(self))
