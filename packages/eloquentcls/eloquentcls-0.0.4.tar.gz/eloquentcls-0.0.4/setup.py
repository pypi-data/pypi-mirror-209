from setuptools import setup, find_packages

setup(
    name='eloquentcls',
    version='0.0.4',
    author='Dr. Shakeel Ahmad Sheikh',
    description='Unimodal Eloquent Classifier',
    py_modules=["__init__", "data_download", "eloquentcls"],
    package_dir={'': 'src'},
    #packages=find_packages(),
    install_requires=[
	'torch>=2.0.1',
   ],

   classifiers=[
	"Programming Language :: Python :: 3.11",
]
)

