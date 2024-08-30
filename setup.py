from setuptools import setup


__version_info__ = (1, 0, 0)
__version__ = '.'.join([str(v) for v in __version_info__])

setup(
    name="Unum",
    version=__version__,
    description="Units in Python",
    author="Carlos Raymundo",
    author_email="carlos.raymundo.luyo@gmail.com",
    url="https://github.com/ray36512/pmd_unit/Unum",
    license="LGPL",
    install_requires=[
        'six'
    ],
    test_suite="tests",
    packages=(
        'unum',
        'unum.units',
        'unum.units.custom',
        'unum.units.others',
        'unum.units.si',
        'tests',
    )
)
