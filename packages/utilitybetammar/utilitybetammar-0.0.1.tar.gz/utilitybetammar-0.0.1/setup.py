from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'ABC Desc'

# Setting up
setup(
    name="utilitybetammar",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    packages=["utilitybetammar"],
    keywords=['python', 'requests', 'sys'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)