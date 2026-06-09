project('mhash', 'c',
  version : '0.9.9.9',
  meson_version : '>=1.3.0',
)

c = meson.get_compiler('c')

global_inc = include_directories('include')

subdir('include')
subdir('lib')

mhash_dep = declare_dependency(
  include_directories : global_inc,
  link_with : mhash_lib,
)
