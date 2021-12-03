import setuptools


def read_version(path='version'):
    with open(path) as file:
        return file.read()


setuptools.setup(
    name='lzy-py',
    version=read_version(),
    author='ʎzy developers',
    include_package_data=True,
    packages=['src/lzy'],
    install_requires=[
        'cloudpickle==2.0.0',
        'pyyaml'
    ],
    python_requires='>=3.7'
)

