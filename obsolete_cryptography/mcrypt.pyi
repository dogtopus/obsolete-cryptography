from typing import Literal, Self
from . import CipherProperty

class MCryptError(OSError):
    @classmethod
    def from_errno(cls, mcrypt_errno: int) -> Self: ...

class MCrypt:
    '''
    Bindings for libmcrypt. Loosely follows PEP-272 API.
    '''

    @property
    def block_size(self) -> int: ...
    @property
    def algorithm(self) -> str: ...
    @property
    def mode(self) -> str: ...
    @property
    def IV(self) -> bytes | None: ...
    @property
    def is_block(self) -> bool: ...
    @property
    def state(self) -> Literal['initialized', 'encrypting', 'decrypting']: ...

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
    Return a dictionary that describes the properties of the selected
    algorithm. The property dictionary contains three keys as follows:

    - `block_size`: The size of block in bytes. For stream ciphers this
      should be 1.
    - `max_key_size`: Maximum size of the key stream in bytes.
    - `accepted_key_sizes`: A `set` of accepted key stream sizes in bytes. This
      is populated when an algorithm supports one or multiple EXACT key sizes
      (e.g. rijndael supports maximum key stream size of 32, but the key stream
      size must be either 16, 24 or 32). If this is not the case i.e. the
      algorithm supports any key stream size from 1 to `max_key_size`, this may
      be empty.
    '''
    ...
