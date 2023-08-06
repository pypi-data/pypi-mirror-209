from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='polishstring',
    version='0.0.2',
    license='MIT',
    description='Polishstring Interconversion',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tanmay Mandal',
    author_email='tanmay.mandal@zohomail.in',
    packages=['polishstring'],
    install_requires=['stringtokenizer'],
    python_requires='>=3.6',
)

