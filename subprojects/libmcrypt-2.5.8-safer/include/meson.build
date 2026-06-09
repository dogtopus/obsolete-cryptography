cfg = configuration_data()

cfg.set('HAVE_BYTESWAP_H', c.has_header('byteswap.h') ? 1 : false)
cfg.set('HAVE_BZERO', c.has_function('bzero', prefix : '#include <strings.h>') ? 1 : false)
cfg.set('HAVE_DIRENT_H', c.has_header('dirent.h') ? 1 : false)
cfg.set('HAVE_ENDIAN_H', c.has_header('endian.h') ? 1 : false)
cfg.set('HAVE_MEMMOVE', c.has_function('memmove', prefix : '#include <string.h>') ? 1 : false)
cfg.set('HAVE_MEMSET', c.has_function('memset', prefix : '#include <string.h>') ? 1 : false)

if c.has_header('sys/mman.h')
  cfg.set('HAVE_SYS_MMAN_H', 1)
  cfg.set('HAVE_MLOCK', c.has_function('mlock', prefix : '#include <sys/mman.h>') ? 1 : false)
else
  cfg.set('HAVE_SYS_MMAN_H', false)
  cfg.set('HAVE_MLOCK', false)
endif

cfg.set('HAVE_READDIR', c.has_function('readdir', prefix : '#include <dirent.h>') ? 1 : false)
cfg.set('HAVE_STRINGS_H', c.has_header('strings.h') ? 1 : false)
cfg.set('HAVE_SYS_ENDIAN_H', c.has_header('sys/endian.h') ? 1 : false)
cfg.set('HAVE_SYS_TYPES_H', c.has_header('sys/types.h') ? 1 : false)
cfg.set('HAVE_UNISTD_H', c.has_header('unistd.h') ? 1 : false)

cfg.set('SIZEOF_UNSIGNED_CHAR', c.sizeof('unsigned char'))
cfg.set('SIZEOF_UNSIGNED_INT', c.sizeof('unsigned int'))
cfg.set('SIZEOF_UNSIGNED_LONG_INT', c.sizeof('unsigned long'))
cfg.set('SIZEOF_UNSIGNED_SHORT_INT', c.sizeof('unsigned short'))

cfg.set('STDC_HEADERS', 1)

cfg.set('VERSION', '"' + meson.project_version() + '"')

if host_machine.endian() == 'big'
  cfg.set('WORDS_BIGENDIAN', 1)
endif

# TODO: win32 flag

configure_file(
  output: 'config.h',
  configuration: cfg,
)

subdir('mutils')
