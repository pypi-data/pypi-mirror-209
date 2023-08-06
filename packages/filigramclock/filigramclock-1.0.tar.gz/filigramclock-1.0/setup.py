from setuptools import setup, find_packages

setup(
    name="filigramclock",
    version="1.0",
    description="Le nouveau time.clock",
    author="CodeurIII",
    author_email="nathan2.che974@gmail.com",
    url="https://github.com/Filigram/myclock",
    packages=find_packages(),
    requires=[
        "datetime",
    ],
)