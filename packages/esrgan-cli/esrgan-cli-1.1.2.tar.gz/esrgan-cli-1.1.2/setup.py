from setuptools import setup

setup(
    name='esrgan-cli',
    version='1.1.2',
    author='Sayantan Das',
    author_email='sdas.codes@gmail.com',
    description='ESRGAN CLI Tool',
    py_modules=['esrgan', 'esrgan_client'],
    install_requires=['requests', 'argparse'],
    entry_points={
        'console_scripts': [
            'esrgan = esrgan:main'
        ]
    }
)
