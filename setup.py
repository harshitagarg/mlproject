from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requierements(file_path)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n",'')  for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements


setup(
    name='mlproject',
    verison='0.1.1',
    author='Harshi',
    author_email='gargharshita24@gmailcom',
    packages=find_packages(),
    install_requires=get_requierements('requirements.txt')
)