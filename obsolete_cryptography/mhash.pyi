from enum import IntEnum, auto

class MHashAlgorithm(IntEnum):
    CRC32 = auto()
    CRC32B = auto()
    ADLER32 = auto()
    MD2 = auto()
    MD4 = auto()
    RIPEMD128 = auto()
    RIPEMD160 = auto()
    RIPEMD256 = auto()
    RIPEMD320 = auto()
    MD5 = auto()
    SHA1 = auto()
    SHA224 = auto()
    SHA256 = auto()
    SHA384 = auto()
    SHA512 = auto()
    HAVAL128 = auto()
    HAVAL160 = auto()
    HAVAL192 = auto()
    HAVAL224 = auto()
    HAVAL256 = auto()
    TIGER128 = auto()
    TIGER160 = auto()
    TIGER192 = auto()
    GOST = auto()
    WHIRLPOOL = auto()
    SNEFRU128 = auto()
    SNEFRU256 = auto()
    AR = auto()
    BOOGNISH = auto()
    CELLHASH = auto()
    FFT_HASH_I = auto()
    FFT_HASH_II = auto()
    NHASH = auto()
    PANAMA = auto()
    SMASH = auto()
    SUBHASH = auto()
    HAVAL = auto()
    TIGER = auto()

class MHash:
    digest_size: int
    algorithm: str
    algorithm_id: int

    def __init__(self, algorithm_id: int, initial_data: bytes | bytearray | None = None) -> None: ...
    def update(self, data: bytes | bytearray) -> None:
        '''
        Hash string into the current state of the hashing object. update() can
        be called any number of times during a hashing object's lifetime.
        '''
        ...
    def digest(self) -> bytes:
        '''
        Return the hash value of this hashing object as a string containing
        8-bit data. The object is not altered in any way by this function;
        you can continue updating the object after calling this function.
        '''
        ...
    def hexdigest(self) -> str:
        '''
        Return the hash value of this hashing object as a string containing
        hexadecimal digits. Lowercase letters are used for the digits a through
        f.
        '''
        ...

def list_algorithms() -> set[str]:
    '''
    List all hash algorithms supported by the library.
    '''
    ...
def get_block_size(algorithm_id: int) -> int:
    '''
    Get hash block size by algorithm ID.
    '''
    ...
