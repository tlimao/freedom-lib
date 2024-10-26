from dataclasses import dataclass
from typing import Any

from freedomlib.utils.serializable import Serializable


@dataclass
class Key(Serializable):
    
    id: str
    aci: str
    ed25519_pub_key: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "aci": self.aci,
            "ed25519_pub_key": self.ed25519_pub_key
        }

    @classmethod
    def from_dict(cls, data: dict) -> Any:
        return Key(
            id=data.get("id"),
            aci=data.get("aci"),
            ed25519_pub_key=data.get("ed25519_pub_key")
        )