from __future__ import annotations

import datetime
import enum
from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Callable, Any, List, Iterator, Sequence

from qprsim.shared.base_classes import FrozenDict


class AttributeLevel(enum.Enum):
    Case = 'case'
    Event = 'event'


@dataclass(unsafe_hash=True)
class CaseEvent:
    activity: str
    resource: str
    timestamp: datetime.datetime
    lifecycle: str = 'complete'
    attributes: FrozenDict[str, Any] = field(default_factory=FrozenDict)

    def __init__(self, activity: str, resource: str, time: datetime.datetime, lifecycle: str = 'complete',
                 **attributes) -> None:
        self.activity = activity
        self.resource = resource
        self.timestamp = time
        self.lifecycle = lifecycle
        self.attributes = FrozenDict(attributes)

    def __str__(self) -> str:
        return f'{self.activity}[{self.lifecycle}] @{self.timestamp.strftime("%Y-%m-%d %H:%M")} by {self.resource} with {self.attributes}'


class AbstractCase(Sequence):

    def __init__(self, case_id: str) -> None:
        super(AbstractCase, self).__init__()
        self.case_id = case_id

    @abstractmethod
    def add_event(self, event: CaseEvent) -> None:
        ...

    @abstractmethod
    def set_case_attribute(self, key: str, value: Any):
        ...

    def project(self, condition: Callable[[CaseEvent], bool] = lambda ce: ce.lifecycle == 'complete',
                projection: Callable[[CaseEvent], Any] = lambda ce: ce.activity) -> AbstractCase:
        ...

    def filter(self, condition: Callable[[CaseEvent], bool]) -> AbstractCase:
        ...

    @abstractmethod
    def get_case_attr_value(self, attr_name: str) -> Any: ...

    @abstractmethod
    def get_latest_event_attr_value(self, attr_name: str) -> Any: ...


class Case(AbstractCase, ABC):

    def __init__(self, case_id: str, **kwargs) -> None:
        super().__init__(case_id)
        self.attributes = kwargs

    def set_case_attribute(self, key: str, value: Any):
        self.attributes[key] = value

    def get_case_attr_value(self, attr_name: str) -> Any:
        return self.attributes.get(attr_name)


# TODO StaticHashable usage, see sim_model
class BaseCase(Case):

    def __init__(self, case_id: str, events: List[CaseEvent] = None, **case_attributes):
        super(BaseCase, self).__init__(case_id, **case_attributes)  # hash_obj=case_id)
        self.events = events if events else []

    def __getitem__(self, i: int) -> CaseEvent:
        return self.events[i]

    def index(self, x: Any, start: int = ..., end: int = ...) -> int:
        return self.events.index(x, start, end)

    def count(self, x: Any) -> int:
        return self.events.count(x)

    def __contains__(self, x: object) -> bool:
        return x in self.events

    def __iter__(self) -> Iterator[CaseEvent]:
        return iter(self.events)

    def __reversed__(self) -> Iterator[CaseEvent]:
        return reversed(self.events)

    def __len__(self) -> int:
        return len(self.events)

    def add_event(self, event: CaseEvent) -> None:
        self.events.append(event)

    def project(self, condition: Callable[[CaseEvent], bool] = lambda ce: ce.lifecycle == 'complete',
                projection: Callable[[CaseEvent], Any] = lambda ce: ce.activity) -> Case:
        projection = projection if projection else lambda ce: ce
        condition = condition if condition else lambda ce: True
        return BaseCase(self.case_id, [projection(event) for event in self.events if condition(event)],
                        **self.attributes)

    def filter(self, condition: Callable[[CaseEvent], bool]) -> Case:
        return BaseCase(self.case_id, [event for event in self.events if condition(event)], **self.attributes)

    def __str__(self) -> str:
        return f'Case(id={self.case_id}, attrs={self.attributes}: ' + ','.join(map(str, self.events)) + ')'

    def __repr__(self) -> str:
        return str(self)

    def get_latest_event_attr_value(self, attr_name: str) -> Any:
        for e in reversed(self):
            if attr_name in e.attributes:
                return e.attributes[attr_name]


class ChildCase(Case):

    def __init__(self, case_id: str, parent_case: Case, **own_case_attributes):
        super(ChildCase, self).__init__(case_id, **own_case_attributes)
        self.parent = parent_case

    def __str__(self) -> str:
        return f'ChildCase(id={self.case_id}, attrs={self.attributes}, parent={self.parent})'

    def __repr__(self):
        return str(self)

    def project(self, condition: Callable[[CaseEvent], bool] = lambda ce: ce.lifecycle == 'complete',
                projection: Callable[[CaseEvent], Any] = lambda ce: ce.activity) -> Case:
        return self.parent.project(condition, projection)

    def filter(self, condition: Callable[[CaseEvent], bool]) -> Case:
        return self.parent.filter(condition)

    def add_event(self, event: CaseEvent) -> None:
        self.parent.add_event(event)

    def get_latest_event_attr_value(self, attr_name: str) -> Any:
        return self.parent.get_latest_event_attr_value(attr_name)

    def __getitem__(self, index: int) -> CaseEvent:
        return self.parent.__getitem__(index)

    def index(self, x: Any, start: int = ..., end: int = ...) -> int:
        return self.parent.index(x, start, end)

    def count(self, x: Any) -> int:
        return self.parent.count(x)

    def __contains__(self, x: object) -> bool:
        return x in self.parent

    def __iter__(self) -> Iterator[CaseEvent]:
        return iter(self.parent)

    def __reversed__(self) -> Iterator[CaseEvent]:
        return reversed(self.parent)

    def __len__(self) -> int:
        return len(self.parent)


def create_case(case_id, initial_events=None, **case_attributes) -> Case:
    return BaseCase(case_id, initial_events, **case_attributes)


def create_child(parent: Case, sub_id: str, **kwargs) -> ChildCase:
    return ChildCase(parent.case_id + '_' + sub_id, parent_case=parent, sub_id=sub_id, **kwargs)
