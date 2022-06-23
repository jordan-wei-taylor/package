# package template

Change variables in the ``setup.py`` file as appropriate. Change ``src/package`` to ``src/your_package_name``.

It is always recommended to have a virtual python environment.

```bash
# create virtual python environment if you do not have one
python3 -m venv env

# activate it
# Mac OS / Linux
source env/bin/activate

# Windows
./env/Scripts/activate
```

To install locally run

```bash
pip install .
```

To upload to pypi install the required libraries first

```bash
pip install build twine
```

and call

```bash
python -m build
twine upload dist/*
```

For more help see this [link](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives) for an example of how to upload to a testing pypi with comments at the bottom on how to upload to pypi.
