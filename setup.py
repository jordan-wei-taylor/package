import setuptools

def read(path):
    with open(path, encoding = 'utf-8') as f:
        return f.read()

username = 'username'
package = 'package'
version = 'version'
author = 'author'
email = 'email'

setuptools.setup(
    name                          = package,
    version                       = version,
    author                        = author,
    author_email                  = email,
    description                   = "A short description of your package",
    long_description              = read('README.md'),
    long_description_content_type = "text/markdown",
    url                           = f"https://github.com/{username}/{package}",
    project_urls                  = {
        "Bug Tracker" : f"https://github.com/{username}/{package}/issues",
                                    },
    classifiers                   = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
                                    ],
    package_dir                   = {"" : "src"},
    package                       = setuptools.find_packages(where = "src"),
    python_requires               = ">=3.8",
    license                       = read('LICENSE'), 
    install_requires              = read('docs/requirements.txt').strip().split()
)
