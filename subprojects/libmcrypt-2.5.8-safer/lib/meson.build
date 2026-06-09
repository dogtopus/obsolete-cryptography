lib_src = [
    'bzero.c',
    'mcrypt_extra.c',
    'mcrypt_modules.c',
    'mcrypt_threads.c',
    'mcrypt.c',
    'xmemory.c',
]

mcrypt_lib = static_library(
    'mcrypt',
    sources: lib_src,
    include_directories: [global_inc],
    link_with: mcrypt_modules_lib,
    pic: true,
)
