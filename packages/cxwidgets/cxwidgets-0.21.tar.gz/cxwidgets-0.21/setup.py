from setuptools import setup, find_packages

setup(
    name='cxwidgets',
    version='0.21',
    author='Fedor Emanov',
    description='PyQt widgets connected to CX v4 control system framewok with designer plugins',
    license='gpl-3.0',
    install_requires=[],
    packages=find_packages(
        #OQwhere='cxwidgets',  # '.' by default
        # include=['mypackage*'],  # ['*'] by default
        # exclude=['mypackage.tests'],  # empty by default
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.0',

)