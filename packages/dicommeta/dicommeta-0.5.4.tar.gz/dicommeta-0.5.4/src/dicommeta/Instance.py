from attr import define, field


@define(kw_only=True, slots=True, order=True, frozen=True)
class Instance:
    SOPinstanceUID: str = field(factory=str)
