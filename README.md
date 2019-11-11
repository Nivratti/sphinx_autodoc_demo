
# Automatic Python documentation with Sphinx autodoc

## Install Sphinx

1. First, install the Sphinx package:

```console
pip install Sphinx
```

2. Next, create a docs directory at the root of your project directory

```console
cd /path/to/project
mkdir docs
```

3. run sphinx-quickstart comamnd

```console
sphinx-quickstart
```

This begins the configuration process. The defaults are generally fine, but the only thing you need to do is enable the autodoc extension when asked.

4. Assuming all of your docstrings have been written, you need to create the stubs for your project in your docs directory (these need to be recreated if new modules are added):

```
sphinx-apidoc -o source/ ../
```

5. Eventually, we’ll be using ReadTheDocs (RTD) to build and host the Python documentation. In order for RTD to find your package files we need to make a change to the Sphinx config. After the quickstart process above, Sphinx should have created a conf.py file in your docs directory. Near the top of that file, you need to add a path to your package contents (or uncomment the lines already in the file):

```python
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(os.path.abspath(BASE_DIR))
sys.path.append(BASE_DIR)  # append the path to system

```

6. In here we can also change the theme of our documentation page:

```
html_theme = 'sphinx_rtd_theme'
```

7. And add extensions:

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]
 
napoleon_google_docstring = True
napoleon_use_param = False
napoleon_use_ivar = True
```

8. Now we can try to build the documentation locally. Sphinx includes a make file that we can use for this:

```
make html
```

9. You may need to install the mock and sphinx_rtd_theme modules for a local build to work:

```
pip install mock
pip install sphinx_rtd_theme
```
