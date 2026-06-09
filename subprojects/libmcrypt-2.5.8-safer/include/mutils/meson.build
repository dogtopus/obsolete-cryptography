# mcrypt.h.in is in the exact format that we wanted. Just reuse it.

cfg_mcrypt = configuration_data()
cfg_mcrypt.set('VERSION', meson.project_version())

configure_file(
  output: 'mcrypt.h',
  input: 'mcrypt.h.in',
  configuration: cfg_mcrypt,
)
