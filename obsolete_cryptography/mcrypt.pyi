from typing import Self
from . import CipherProperty

class MCryptError(OSError):
    @classmethod
    def from_errno(cls, mcrypt_errno: int) -> Self: ...

class MCrypt:
    '''
    Bindings for libmcrypt. Loosely follows PEP-272 API.
    '''

    block_size: int
    algorithm: str
    mode: str
    IV: bytes | None
    is_block: bool

    def __init__(self, algorithm: str, key: bytes | bytearray, mode: str, iv: bytes | bytearray | None = None) -> None: ...
    def self_test(self) -> None:
        '''
        Perform mcrypt self test.
        Raises MCryptError when self test fails.
        '''
        ...
    def encrypt(self, data: bytes | bytearray) -> bytes:
        '''
        Encrypt data.
        For a cipher in block mode the data must be aligned to the block size.
        '''
        ...
    def decrypt(self, data: bytes | bytearray) -> bytes:
        '''
        Decrypt data.
        For a cipher in block mode the data must be aligned to the block size.
        '''
        ...

def list_algorithms() -> set[str]:
    '''
    List all ciphers supported by the library.
    '''
    ...
def list_modes() -> set[str]:
    '''
    List all modes supported by the library.
    '''
    ...
def get_algorithm_props(algorithm_name: str) -> CipherProperty:
    '''
    Return a dictionary that describes the properties of the selected algorithm.
    '''
    ...
