from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='stringtokenizer',
    version='1.1.1',
    description='A string tokenizer implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tanmay Mandal',
    packages=['stringtokenizer'],
    python_requires='>=3.6',
)

