""" 上传 pypi """

import setuptools

from tkintertools import __version__

mode = 1
# 0 : 正式版
# 1 : 开发版
# 2 : 测试版

name = ('tkintertools', 'tkintertools_dev', 'tkintertools_test')[mode]
version = __version__ if mode == 0 else input(
    '输入%s版本号: ' % ('开发' if mode == 1 else '测试'))

setuptools.setup(
    name=name,
    version=version,
    author='Xiaokang2022',
    author_email='2951256653@qq.com',
    description='An auxiliary module of the tkinder module',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://gitcode.net/weixin_62651706/tkintertools',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Mulan Permissive Software License v2 (MulanPSL-2.0)',
        'Operating System :: OS Independent',
    ],
)

# python -m pip install --user --upgrade setuptools wheel [检查更新]
# python setup.py sdist bdist_wheel [打包]
# twine upload dist/* [上传]

# pip install -U pypistats [数据分析]
# pip install socksio [数据分析]

# pypistats overall tkintertools [数据分析]
# pypistats recent tkintertools
# pypistats system tkintertools
# pypistats python_minor tkintertools
# pypistats python_major tkintertools

# https://pypistats.org/packages/tkintertools [数据分析]
