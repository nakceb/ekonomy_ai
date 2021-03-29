from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="filip_python_economy",
    version="0.0.1",
    author="Filip Stenbeck",
    author_email="filip.stenbeck@hotmail.com",
    description="Some classes to help with queering data from the alpha vantage",
    scripts=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['alpha_vantage'],
    include_package_data=True,
    install_requires=[
        'pandas==1.1.3',
        'numpy==1.19.2',
        'plotly==4.11.0',
      ],
    python_requires='>=3.6',
)
