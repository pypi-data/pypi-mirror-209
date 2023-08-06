from setuptools import setup, find_packages

setup(
    name="nmping",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # e.g., 'numpy >= 1.13.3'
    ],
    author="Pierre Gode",
    author_email="pierre@gode.one",
    description="This is an Example Package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/PierreGode/Nmping",
    classifiers=[
        # List classifiers: https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
