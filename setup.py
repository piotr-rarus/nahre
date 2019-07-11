import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='nahre',
    version='0.1.0',
    author='Piotr Rarus',
    author_email='p.rarus@micro-solutions.pl',
    description='CV research lib.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://msol-git:3000/ai-tools/nahre',
    packages=setuptools.find_packages(
        exclude=[
            "tests",
            "examples"            
        ]
    ),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-image',
        'pytest',
        'lazy_property',
        'tqdm',
    ],
)
