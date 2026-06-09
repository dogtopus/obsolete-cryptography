# Generate configuration file
CFG_MAPPING = {
  'adler32': 'ENABLE_ADLER32',
  'crc32': 'ENABLE_CRC32',
  'gost': 'ENABLE_GOST',
  'haval': 'ENABLE_HAVAL',
  'md2': 'ENABLE_MD2',
  'md4': 'ENABLE_MD4',
  'md5': 'ENABLE_MD5',
  'ripemd': 'ENABLE_RIPEMD',
  'sha1': 'ENABLE_SHA1',
  'sha256_sha224': 'ENABLE_SHA256_SHA224',
  'sha512_sha384': 'ENABLE_SHA512_SHA384',
  'snefru': 'ENABLE_SNEFRU',
  'tiger': 'ENABLE_TIGER',
  'whirlpool': 'ENABLE_WHIRLPOOL',
}

cfg = configuration_data()

foreach opt, ckey : CFG_MAPPING
  if get_option(opt)
    cfg.set(ckey, 1)
  endif
endforeach

# We only care about flags that are actually referenced elsewhere in the code (like conditional includes and uses)
# Compiler sanity checks generally aren't included here
cfg.set('HAVE_ASSERT_H', c.has_header('assert.h') ? 1 : false)
cfg.set('HAVE_CTYPE_H', c.has_header('ctype.h') ? 1 : false)
cfg.set('HAVE_ERRNO_H', c.has_header('errno.h') ? 1 : false)
cfg.set('HAVE_INTTYPES_H', c.has_header('inttypes.h') ? 1 : false)
cfg.set('HAVE_LIMITS_H', c.has_header('limits.h') ? 1 : false)
cfg.set('HAVE_MALLOC_H', c.has_header('malloc.h') ? 1 : false)

# Autotools also checks for conformity but we likely don't need to go that far.
if c.has_header('stdbool.h')
  cfg.set('HAVE_STDBOOL_H', 1)
  cfg.set('HAVE__BOOL', c.has_type('_Bool', prefix : '#include <stdbool.h>') ? 1 : false)
else
  cfg.set('HAVE_STDBOOL_H', false)
  cfg.set('HAVE__BOOL', false)
endif

cfg.set('HAVE_STDINT_H', c.has_header('stdint.h') ? 1 : false)
cfg.set('HAVE_STDIO_H', c.has_header('stdio.h') ? 1 : false)
cfg.set('HAVE_STDLIB_H', c.has_header('stdlib.h') ? 1 : false)
cfg.set('HAVE_STRINGS_H', c.has_header('strings.h') ? 1 : false)
cfg.set('HAVE_STRING_H', c.has_header('string.h') ? 1 : false)

if c.has_header('sys/mman.h')
  cfg.set('HAVE_SYS_MMAN_H', 1)
  cfg.set('HAVE_MLOCK', c.has_function('mlock', prefix : '#include <sys/mman.h>') ? 1 : false)
else
  cfg.set('HAVE_SYS_MMAN_H', false)
  cfg.set('HAVE_MLOCK', false)
endif

cfg.set('HAVE_SYS_TYPES_H', c.has_header('sys/types.h') ? 1 : false)
cfg.set('HAVE_UNISTD_H', c.has_header('unistd.h') ? 1 : false)
cfg.set('HAVE_VALUES_H', c.has_header('values.h') ? 1 : false)

cfg.set('PROTOTYPES', 1)
cfg.set('STDC_HEADERS', 1)

if host_machine.endian() == 'big'
  cfg.set('WORDS_BIGENDIAN', 1)
endif

if not c.has_type('size_t', prefix : '#include <sys/types.h>')
  cfg.set('size_t', 'unsigned int')
endif

# TODO: win32 flag

mhash_config = configure_file(
  output: 'mhash_config.h',
  configuration: cfg,
)

# Header installation list
inc = [
  'mglobal.h',
  'mhash.h',
  'mincludes.h',
  'mtypes.h',
  'mutils.h',
  mhash_config,
]

install_headers(inc, subdir : 'mutils')
