from setuptools import setup

setup(
    name='vkbasalt-cli',
    version='v3.1.1',
    packages=['vkbasalt'],
    url='https://gitlab.com/TheEvilSkeleton/vkbasalt-cli',
    license='LGPLv3',
    author='TheEvilSkeleton',
    author_email='theevilskeleton@riseup.net',
    description='A utility to pass arguments to vkBasalt',
    entry_points={
        'console_scripts': [
            'vkbasalt=vkbasalt.cli:vkbasalt_cli'
        ]
    },
)
