import setuptools
import shutil

def read(path):
    with open(path, encoding = 'utf-8') as f:
        return f.read()

username = 'jordan-wei-taylor'
name     = 'package'
version  = '0.0.1'
author   = 'Jordan Taylor'
email    = 'jt2006@bath.ac.uk'

setuptools.setup(
    name                          = name,
    version                       = version,
    author                        = author,
    author_email                  = email,
    description                   = "A short description of your package",
    long_description              = read('README.md'),
    long_description_content_type = "text/markdown",
    url                           = f"https://github.com/{username}/{name}",
    project_urls                  = {
        "Bug Tracker" : f"https://github.com/{username}/{name}/issues",
                                    },
    classifiers                   = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
                                    ],
    package_dir                   = {"" : "src"},
    package                       = setuptools.find_packages(where = "src"),
    python_requires               = ">=3.6",
    license                       = read('LICENSE'), 
    install_requires              = [
        # 'numpy>=1.22.3', # example requirements
        # 'psutil>=5.9.0',
                                    ]
)

# shutil.rmtree(f'src/{name}.egg-info')