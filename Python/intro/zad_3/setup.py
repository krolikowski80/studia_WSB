# Importujemy niezbędne funkcje z biblioteki setuptools
# setup() - główna funkcja konfiguracyjna do pakietu
# find_packages() - automatycznie znajduje wszystkie pakiety i moduły w projekcie
from setuptools import setup, find_packages

# Wywołanie funkcji setup() - tutaj podajemy wszystkie dane o naszym pakiecie
setup(
    # Nazwa biblioteki (ważne przy publikacji np. do PyPI)
    name='my_awesome_lib',

    # Wersja biblioteki - dobre praktyki: major.minor.patch
    version='0.1',

    # Automatyczne wykrywanie wszystkich pakietów (folderów z __init__.py)
    packages=find_packages(),

    # Zależności wymagane do działania biblioteki
    # Tu np. można wpisać: ['numpy', 'pandas'] jeśli pakiet ich wymaga
    install_requires=[],

    # Informacje o autorze - do dokumentacji i informacji o pakiecie
    author='Tomasz Królikowski',
    author_email='t.krolikowski@gmail.com',

    # Krótki opis biblioteki - wyświetlany np. na PyPI
    description='Przykładowa biblioteka w Pythonie do labów WSB',

    # Długi opis biblioteki - tutaj wczytujemy treść z pliku README.md
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',

    # Adres URL do repozytorium
    url='https://github.com/twój_login/my_awesome_lib',

    # Klasyfikatory - meta dane pakietu według standardów PyPI
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Requires-Python >=3.8',
    ],
)