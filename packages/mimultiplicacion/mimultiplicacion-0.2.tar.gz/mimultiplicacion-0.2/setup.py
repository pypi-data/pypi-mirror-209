import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    # ######################################################################
    # BASIC DESCRIPTION
    # ######################################################################
    name='mimultiplicacion',
    author='Juani',
    author_email='juanita.agudelo@udea.edu.co',
    description='Make a multiplicacion',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://pypi.org/project/mimultiplicacion',
    keywords='multiplication maths',
    license='MIT',

    # ######################################################################
    # CLASSIFIER
    # ######################################################################
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
    version='0.2',

    # ######################################################################
    # FILES
    # ######################################################################
    package_dir={'': '.'},
    packages=setuptools.find_packages(where='.'),
    
    # ######################################################################
    # ENTRY POINTS
    # ######################################################################
    entry_points={
        'console_scripts': ['install=mimultiplicacion.install:main'],
    },

    # ######################################################################
    # TESTS
    # ######################################################################
    test_suite='nose.collector',
    tests_require=['nose'],

    # ######################################################################
    # DEPENDENCIES
    # ######################################################################
    install_requires=['numpy', 'matplotlib'],

    # ######################################################################
    # OPTIONS
    # ######################################################################
    include_package_data=True,
    package_data={'': ['data/*.*', 'tests/*.*']},
)
