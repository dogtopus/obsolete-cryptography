framework_src = [
  'mhash.c',
  'stdfns.c',
]

keygen_src = [
  'keygen_hex.c',
  'keygen_mcrypt.c',
  'keygen_asis.c',
  'keygen.c',
  'keygen_s2k.c',
]

crc_src = [
  'crc32.c',
  'adler32.c',
]

md_series_src = [
  'md2.c',
  'md4.c',
  'md5.c',
  'ripemd.c',
]

sha_series_src = [
  'sha1.c',
  'sha256_sha224.c',
  'sha512_sha384.c',
]

tiger_src = [
  'tiger.c',
  'tiger_sboxes.c',
]

miscellaneous_src = [
  'haval.c',
  'gosthash.c',
  'whirlpool.c',
  'snefru.c',
]

all_src = [
  framework_src,
  keygen_src,
  crc_src,
  md_series_src,
  sha_series_src,
  tiger_src,
  miscellaneous_src,
]

mhash_lib = static_library(
  'mhash',
  sources: all_src,
  include_directories: [global_inc],
  install: true,
  pic: true,
)
