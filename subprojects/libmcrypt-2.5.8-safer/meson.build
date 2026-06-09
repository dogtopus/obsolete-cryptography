project('mcrypt', 'c',
    version : '2.5.8',
    meson_version : '>=1.3.0',
)

c = meson.get_compiler('c')
python = import('python').find_installation('python3')

add_project_arguments('-DHAVE_CONFIG_H', language : 'c')
add_project_arguments('-DLIBDIR=""', language : 'c')

global_inc = include_directories(['include', 'lib', '.'])

subdir('include')
subdir('modules')
subdir('lib')

mcrypt_dep = declare_dependency(
    include_directories : global_inc,
    link_with : mcrypt_lib,
)
