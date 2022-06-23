# package template

A template repository for a python package with a readthedocs style website.

First run the setup file and enter your details

```bash
./setup
```

Next, ``source`` the ``activate`` file to switch to a virtual python environment and have access to the functions ``build-website`` and ``view-website``.

```bash
source 
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
