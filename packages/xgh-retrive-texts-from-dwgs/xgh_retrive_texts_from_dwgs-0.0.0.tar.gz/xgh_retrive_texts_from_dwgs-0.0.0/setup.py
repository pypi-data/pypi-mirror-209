from setuptools import setup, find_packages
with open('./README.md', encoding='utf8') as f:
    description = f.read()
setup(
    name='xgh_retrive_texts_from_dwgs',
    version='0.0.0',
    description=description,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'x-retrieve-texts-from-dwgs=retrieve_texts_from_dwgs.retrieve_texts_from_dwgs:main'
        ]
    }
)
