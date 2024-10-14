from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from freedomlib.utils.serializable import Serializable


@dataclass(frozen=True)
class Message(Serializable):

    id: str
    sender_aci: str
    recipient_aci: str
    nonce: bytes
    tag: bytes
    cipher_message: bytes
    timestamp: int = field(default_factory=lambda: int(datetime.now().timestamp()))
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sender_aci": self.sender_aci,
            "recipient_aci": self.recipient_aci,
            "timestamp": self.timestamp,
            "nonce": Serializable.bytes_to_str(self.nonce),
            "tag": Serializable.bytes_to_str(self.tag),
            "cipher_message": Serializable.bytes_to_str(self.cipher_message)
        }

    @classmethod
    def from_dict(cls, data: dict) -> Any:
        return Message(
            id=data.get("id"),
            sender_aci=data.get("sender_aci"),
            recipient_aci=data.get("recipient_aci"),
            timestamp=data.get("timestamp"),
            nonce=Serializable.str_to_bytes(data.get("nonce")),
            tag=Serializable.str_to_bytes(data.get("tag")),
            cipher_message=Serializable.str_to_bytes(data.get("cipher_message"))
        )