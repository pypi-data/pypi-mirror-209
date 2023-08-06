import setuptools
from pathlib import Path

setuptools.setup(
    name='hjj_ur',
    version='0.0.1',
    description='An OpenAI Gym Env for Ur',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(include='gym_ur*'),
    install_requires=['gym']
)