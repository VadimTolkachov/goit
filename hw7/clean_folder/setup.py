from setuptools import setup, find_namespace_packages

setup(
    name='useful',
    version='1',
    description='My code for homework numver 7',
    url='http://github.com/dummy_user/useful',
    author='Flying Circus',
    author_email='curlic_curlic@for_exampel.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean folder = useful.some_code:sort']}
)