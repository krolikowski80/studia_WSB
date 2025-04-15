# Plik __init__.py informuje Pythona, że katalog my_awesome_lib jest pakietem.
# Dzięki temu możemy importować nasze moduły jak prawdziwą bibliotekę.

# Przykładowo:
# from my_awesome_lib import math_tools, data_utils, text_processing

# Możemy też bezpośrednio zaimportować wszystko tutaj
# aby ułatwić użytkownikowi korzystanie z pakietu:

from . import math_tools
from . import data_utils
from . import text_processing
