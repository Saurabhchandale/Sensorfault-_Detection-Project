from setuptools import find_packages,setup
from typing import List

HYPAN_E_DOT='-e .'

# define function
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
    if HYPAN_E_DOT in requirements:
        requirements.remove('HYPAN_E_DOT')
    return requirements


setup(
    name="Sansor_Fault_Detecter",
    version='0.0.1',
    author='Saurrabh',
    author_mail='chandalesaurabh6@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packeages=find_packages()
)


# python setup.py install