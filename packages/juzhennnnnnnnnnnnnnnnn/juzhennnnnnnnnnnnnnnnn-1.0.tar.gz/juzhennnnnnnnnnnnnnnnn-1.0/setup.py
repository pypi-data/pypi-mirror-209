from setuptools import setup, Extension

extension_mod = Extension(
    'matrix_package.matrix',
    sources=['matrix_package/matrix.c'],
    include_dirs=['C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/include']
)

setup(
    name='juzhennnnnnnnnnnnnnnnn',
    version='1.0',
    ext_modules=[extension_mod],
    packages=['matrix_package'],
    package_data={'matrix_package': ['matrix.so']}
)
