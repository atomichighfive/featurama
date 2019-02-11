import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="featurama-atomichighfive",
    version="1.0",
    author="Andreas Syrén",
    author_email="filipandreassyren@gmail.com",
    description="Utilities for effective feature engineering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atomichighfive/featurama",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
          'pandas',
          'numpy',
          'dask',
          'scikit-learn'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
