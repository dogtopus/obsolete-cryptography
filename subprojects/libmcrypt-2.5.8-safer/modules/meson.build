modules_algorithms_src = [
  'algorithms/arcfour.c',
  'algorithms/blowfish.c',
  'algorithms/blowfish-compat.c',
  'algorithms/cast-128.c',
  'algorithms/cast-256.c',
  'algorithms/des.c',
  'algorithms/enigma.c',
  'algorithms/gost.c',
  'algorithms/loki97.c',
  'algorithms/panama.c',
  'algorithms/rc2.c',
  'algorithms/rijndael-128.c',
  'algorithms/rijndael-192.c',
  'algorithms/rijndael-256.c',
  'algorithms/saferplus.c',
  'algorithms/safer-sk128.c',
  'algorithms/safer-sk64.c',
  'algorithms/serpent.c',
  'algorithms/threeway.c',
  'algorithms/tripledes.c',
  'algorithms/twofish.c',
  'algorithms/wake.c',
  'algorithms/xtea.c',
]

modules_modes_src = [
  'modes/cbc.c',
  'modes/cfb.c',
  'modes/ctr.c',
  'modes/ecb.c',
  'modes/ncfb.c',
  'modes/nofb.c',
  'modes/ofb.c',
  'modes/stream.c',
]

symb_src = custom_target(
  'symb',
  command: [python, '@CURRENT_SOURCE_DIR@/gen_symb_table.py', '@OUTPUT@', '@INPUT@'],
  output: 'symb.c',
  input: [modules_modes_src, modules_algorithms_src],
)

mcrypt_modules_lib = static_library(
  'mcrypt_modules',
  sources: [
    modules_modes_src,
    modules_algorithms_src,
    symb_src,
  ],
  include_directories: [global_inc],
  pic: true,
)
