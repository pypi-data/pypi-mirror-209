from setuptools import setup, find_packages
import os


def read(filename):
    # if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as myfile:
        return myfile.read()
    # else:
    #     return ""

setup(name='template-pptx-jinja-fix',
    version="0.0.6",
    description='PowerPoint presentation builder from template using Jinja2',
    long_description=read('readme.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/macheal/template-pptx-jinja',
    author='wlx',
    author_email='409673593@qq.com',
    install_requires=read('requirements.txt').split(),
    license='',
    packages=find_packages(),
    package_data={
        'template-pptx-jinja': ['readme.md','requirements.txt'],
    },
    keywords=['powerpoint', 'ppt', 'pptx', 'template'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ]
)
