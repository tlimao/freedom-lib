from abc import ABC, abstractmethod

from freedomlib.key.key import Key


class KeyRepository(ABC):

    @abstractmethod
    def get(self, key_id: str) -> Key:
        raise NotImplementedError()

    @abstractmethod
    def get_key_by_aci(self, aci: str) -> Key:
        raise NotImplementedError()
    
    @abstractmethod
    def save(self, key: Key) -> Key:
        raise NotImplementedError()

    @abstractmethod
    def update(self, key: Key) -> Key:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, key_id: str) -> None:
        raise NotImplementedError()