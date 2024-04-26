"""
    DFL-DictionaryFormatList

By using a dictionary type,
long, complex, and difficult to read List type data
is made one-dimensional and simplified.
"""

# import
import sys


__self_name__: str = "DFL"


if not __name__ == __self_name__:
    print("Execution failed")
    sys.exit()


try:
    from DFL.dfl import create_tag
    ...
except ImportError as message:
    create_tag = ImportError(message)
    ...


try:
    from DFL.dfl import DFL
    ...
except ImportError as message:
    DFL = ImportError(message)
    ...


try:
    from DFL.dfl import create_dfl
    ...
except ImportError as message:
    create_dfl = ImportError(message)
    ...


try:
    from DFL.dfl import read_dfl
    ...
except ImportError as message:
    read_dfl = ImportError(message)
    ...


print(f"**Initialize {__self_name__}**")
