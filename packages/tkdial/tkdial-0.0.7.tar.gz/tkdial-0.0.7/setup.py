from setuptools import setup

def get_long_description(path):
    """Opens and fetches text of long descrition file."""
    with open(path, 'r') as f:
        text = f.read()
    return text

setup(
    name = 'tkdial',
    version = '0.0.7',
    description = "Rotatory dial-knob widgets for Tkinter.",
    license = "Creative Commons Zero v1.0 Universal",
    readme = "README.md",
    long_description = get_long_description('README.md'),
    long_description_content_type = "text/markdown",
    author = 'Akash Bora',
    url = "https://github.com/Akascape/TkDial",
    classifiers = [
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords = ['tkinter', 'tkinter-dial', 'tkinter-widget',
                'tkinter-knob', 'tkinter-meter', 'tkinter-dial-knob',
                'dial-knob-widget', 'tkinter-gui'],
    packages = ["tkdial"],
    install_requires = ['colour', 'pillow'],
    dependency_links = ['https://pypi.org/project/colour/', 'https://pypi.org/project/Pillow/'],
    python_requires = '>=3.6',
)
