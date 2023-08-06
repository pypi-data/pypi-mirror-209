import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cicpy",
    version="0.1.6",
    author="Carsten Wulff",
    author_email="carsten@wulff.no",
    description="Custom IC Creator Python Frontend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wulffern/cicpy",
    packages=['cicpy'],
    python_requires='>=3.8',
    entry_points = {'console_scripts': [
        'cicpy = cicpy.cic:cli',
    ]},
    install_requires = 'matplotlib numpy click svgwrite pyyaml pandas'.split(),
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering',
    ],
)
