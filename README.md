# my-cpp-lexer
Extension of pygments CppLexer to use custom types.
Types used are for a custom project, but can be easily extended by changing `pygments_mycpp/__init__.py:25`

# Installation
```bash
    $ git clone git@github.com:/florian-world/my-cpp-lexer
    $ cd my-cpp-lexer
    $ (sudo) python setup.py install
```
# Usage

Specify `mycpp` instead of `cpp` as lexer in the latex document.
```latex
    \inputminted{mycpp}{listings/example.cpp}
```
