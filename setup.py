from setuptools import setup,find_packages
from typing import List
h='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if h in requirements:
            requirements.remove(h)
        return requirements


setup(
    name="MLproject",
    version='0.0.1',
    author='Sachin Venkat',
    author_email='tsachinvenkat52@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)