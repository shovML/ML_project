from setuptools import find_packages,setup
from typing import List
 
def get_requirements(file_path: str) -> list[str]:
    '''This function will return a list of requirements'''
    HYPHEN_E_DOT = '-e .'
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
        if HYPHEN_E_DOT in requirements:
          requirements.remove(HYPHEN_E_DOT)
    
    return requirements


# Usage example
file_path = 'requirements.txt'
requirements_list = get_requirements(file_path)
print(requirements_list)




setup(
    name="ML_project",
    version="0.01",
    author='Shubham U',
    author_email='shubhamukey628@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)