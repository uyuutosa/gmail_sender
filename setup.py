from setuptools import setup, find_packages

requires = ["requests>=2.14.2"]


setup(
    name='gmail_sender',
    version='0.1.2',
    description='Simple Email sender with Gmail',
    url='https://github.com/uyuutosa/gmail_sender',
    author='uyuutosa',
    author_email='sayu819@gmail.com',
    keywords='gmail',
    packages=find_packages(),
    install_requires=["emoji"],
    classifiers=[
                'Programming Language :: Python :: 3.6',
            ],
)
