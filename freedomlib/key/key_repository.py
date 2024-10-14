from abc import ABC, abstractmethod

from freedomlib.key.key import Key


class KeyRepository(ABC):

    @abstractmethod
    def get(self, key_id: str) -> Key:
        ...

    @abstractmethod
    def get_key_by_account_id(self, account_id: str) -> Key:
        ...
    
    @abstractmethod
    def save(self, key: Key) -> None:
        ...

    @abstractmethod
    def update(self, key: Key) -> Key:
        ...

    @abstractmethod
    def delete(self, key_id: str) -> None:
        ...