import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='nahre',
    version='0.1.0',
    author='Piotr Rarus',
    author_email='piotr.rarus@gmail.com',
    description='Computer vision research lib.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://msol-git:3000/ai-tools/nahre',
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
