modules_algorithms_src = [
  'algorithms/threeway.c',
  'algorithms/cast-128.c',
  'algorithms/gost.c',
  'algorithms/rijndael-128.c',
  'algorithms/safer-sk64.c',
  'algorithms/twofish.c',
  'algorithms/arcfour.c',
  'algorithms/cast-256.c',
  'algorithms/loki97.c',
  'algorithms/rijndael-192.c',
  'algorithms/saferplus.c',
  'algorithms/wake.c',
  'algorithms/blowfish-compat.c',
  'algorithms/des.c',
  'algorithms/rijndael-256.c',
  'algorithms/serpent.c',
  'algorithms/xtea.c',
  'algorithms/blowfish.c',
  'algorithms/enigma.c',
  # 'algorithms/panama.c',
  'algorithms/rc2.c',
  'algorithms/safer-sk128.c',
  'algorithms/tripledes.c',
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
  command: [python, '@INPUT@', '-o', '@OUTPUT@'],
  output: 'symb.c',
  input: ['gen_symb_table.py', modules_modes_src, modules_algorithms_src],
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
