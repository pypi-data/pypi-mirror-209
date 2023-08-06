from dataclasses import dataclass, fields
from typing import Any, Dict, Type


@dataclass
class FieldFromFile:
    type:Type
    default: Any
    description:str


class Base:
    def fill_config_pre(self, update_dict:Dict[str, Any]) -> None:
        pass

    def fill_config_post(self, update_dict:Dict[str, Any]) -> None:
        pass

    def to_dict_post(self, output:Dict[str, Any]) -> None:
        pass


class Extendable(Base):
    def fill_config_post(self, update_dict:Dict[str, Any]) -> None:
        if not update_dict:
            return

        if not getattr(self, "__extra_config", None):
            setattr(self, "__extra_config", {})

        for name, value in update_dict.items():
            getattr(self, "__extra_config")[name] = value

        super().fill_config_post(update_dict)

    def to_dict_post(self, output:Dict[str, Any]) -> None:
        extra_config = getattr(self, "__extra_config", {})
        for name, value in extra_config.items():
            output[name] = value

        super().to_dict_post(output)

class Configurable(Base):
    def fill_config(self, update_dict:Dict[str, Any], enforce_required:bool=True, root:str="") -> None:
        update_dict = update_dict.copy()
        super().fill_config_pre(update_dict)

        for config_field in fields(self):
            field_value = getattr(self, config_field.name)
            key = f"{root}.{config_field.name}"

            if config_field.name not in update_dict:
                if config_field.metadata.get("required") and enforce_required:
                    raise KeyError(f"Missing mandatory field in configuration: {key}")
                continue

            if isinstance(field_value, Configurable):
                field_value.fill_config(update_dict.pop(config_field.name), enforce_required, key)
            else:
                value = update_dict.pop(config_field.name)
                setattr(self, config_field.name, value)

        super().fill_config_post(update_dict)

    def to_dict(self, from_file:bool=False) -> Dict[str, Any]:
        output = {}

        for config_field in fields(self):
            field_value = getattr(self, config_field.name)
            if isinstance(field_value, Configurable):
                child_config = getattr(self, config_field.name)
                child_config_dict = child_config.to_dict(from_file)
                if not from_file or child_config_dict:
                    output[config_field.name] = child_config_dict

            elif not from_file or (from_file and config_field.metadata.get("from_file")):
                output[config_field.name] = getattr(self, config_field.name)

        super().to_dict_post(output)
        return output

    def get_from_file_params(self) -> Dict[str, FieldFromFile]:
        output = {}

        for config_field in fields(self):
            field_value = getattr(self, config_field.name)
            if isinstance(field_value, Configurable):
                if child_config := getattr(self, config_field.name):
                    output[config_field.name] = child_config.get_from_file_params()

            elif config_field.metadata.get("from_file"):
                output[config_field.name] = FieldFromFile(
                    type=type(field_value),
                    default=config_field.default,
                    description=config_field.metadata.get("description", "")
                )

        return output
