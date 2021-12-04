import pathlib
from collections import namedtuple
from dataclasses import dataclass

from datetime import datetime

import setuptools


@dataclass
class PackageConf:
    name: str
    @property
    def version(self):
        return read_version()


class DevPackageConf(PackageConf):
    def version(self):
        return read_version() + 'dev' + datetime.today().strftime('%Y%m%d')


def read_version(path='version'):
    with open(path) as file:
        return file.read()


conf_map = {
    'refs/heads/master': PackageConf('lzy-py'),
    'refs/heads/dev': DevPackageConf('lzy-dev-py')
}


def _get_git_ref():
    git_head_path = pathlib.Path(__file__).parent / '.git' / 'HEAD'
    with git_head_path.open('r') as git_head:
        return git_head.readline().split()[-1]


try:
    conf = conf_map[_get_git_ref()]
except:
    raise ValueError("Trying to install from other branches than master or dev")


setuptools.setup(
    name=conf.name,
    version=conf.version,
    author='ʎzy developers',
    include_package_data=True,
    packages=['src/lzy'],
    install_requires=[
        'cloudpickle==2.0.0',
        'pyyaml'
    ],
    # cmdclass={
    #     'install': InstallCommand
    # },
    python_requires='>=3.7'
)
