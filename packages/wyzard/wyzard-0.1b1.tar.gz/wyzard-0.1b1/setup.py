from setuptools import setup, find_packages
import re

with open('README.md') as f:
    long_description = f.read()

version = ''
with open('wyzard/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set')

def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name='wyzard',
    version=version,
    author='LyQuid',
    author_email='lyquidpersonal@gmail.com',
    description='Run various transformers models from one packages.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    url='https://github.com/LyQuid12/Wyzard',
    project_urls={
        "Source Code": "https://github.com/LyQuid12/Wyzard",
        "Discord": "https://discord.gg/qpT2AeYZRN",
        "Issue tracker": "https://github.com/LyQuid12/Wyzard/issues"
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    keywords=["python", "machine learning", "ml", "ai", "artificial intelligence", "transformers", "pytorch", "models", "tokenizer"],
    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux"
    ]
)
