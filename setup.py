from setuptools import setup, find_packages

setup(
    name="volkswagen",
    version="0.1.1",
    author="L3viathan",
    author_email="git@l3vi.de",
    description="Detect when your tests run in a CI and make them pass",
    url="https://github.com/L3viathan/pyvw",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
)
