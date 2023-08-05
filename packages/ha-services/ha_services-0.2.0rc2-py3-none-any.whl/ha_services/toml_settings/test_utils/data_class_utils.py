import dataclasses
from pathlib import Path


def replace_dataclass_values(instance, *, data: dict):
    """
    Replace dataclass values in-place with values from given dict.
    """
    assert dataclasses.is_dataclass(instance), f'{instance=}'

    for key, value in data.items():
        if isinstance(value, dict):
            sub_dataclass = getattr(instance, key)
            replace_dataclass_values(sub_dataclass, data=value)
        else:
            assert hasattr(instance, key), f'Attribute "{key}" missing on: {instance=}'
            setattr(instance, key, value)


def replace_path_values(instance):
    assert dataclasses.is_dataclass(instance), f'{instance=}'

    data = dataclasses.asdict(instance)
    for key, value in data.items():
        if isinstance(value, dict):
            sub_dataclass = getattr(instance, key)
            replace_path_values(sub_dataclass)
        elif isinstance(value, Path):
            setattr(instance, key, str(value))
