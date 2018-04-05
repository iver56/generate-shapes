from setuptools import setup

setup(
    name='generate-shapes',
    version='0.1.0',
    packages=['generate_shapes', ],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'numpy',
        'scipy',
        'scikit-image',
    ],
)
