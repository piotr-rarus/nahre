import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='nahre',
    version='0.1.1',
    author='Piotr Rarus',
    author_email='piotr.rarus@gmail.com',
    description='Computer vision research lib.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/piotr-rarus/nahre',
    packages=setuptools.find_packages(
        exclude=[
            "tests"
        ]
    ),
    install_requires=[
        'numpy',
        'scikit-image',
        'austen',
        'degas'
        'lazy',
        'tqdm',
    ],
)
