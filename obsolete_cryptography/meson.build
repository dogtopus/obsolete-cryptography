# Native extensions
py3.extension_module(
    'mcrypt',
    'mcrypt.pyx',
    dependencies : [
        py3_dep,
        mcrypt_dep,
    ],
    install : true,
    subdir : 'obsolete_cryptography',
    limited_api : '3.10',
)

py3.extension_module(
    'mhash',
    'mhash.pyx',
    dependencies : [
        py3_dep,
        mhash_dep,
    ],
    install : true,
    subdir : 'obsolete_cryptography',
    limited_api : '3.10',
)

# Pure Python modules and type stubs
py3.install_sources(
    [
        '__init__.py',
        'mcrypt.pyi',
        'mhash.pyi',
        'py.typed',
    ],
    subdir : 'obsolete_cryptography',
)
