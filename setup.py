from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = "-e ."
def get_requirement(file_path:str)-> list[str]:
    """
    This function will return the list of requirements
    """
    requirement=[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        [req.replace("\n", "") for req in requirement]
        
    if HYPEN_E_DOT in requirement:
        requirement.remove(HYPEN_E_DOT)

setup(
    name="mlproject",
    version="0.1.0",
    description="A machine learning project template",
    author="vishal",
    author_email="vishalsharma122003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirement.txt")
)