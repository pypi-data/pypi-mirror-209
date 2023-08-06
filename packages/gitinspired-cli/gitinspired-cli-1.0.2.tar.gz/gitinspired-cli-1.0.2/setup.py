from setuptools import setup, find_packages

setup(
    name="gitinspired-cli",
    version="1.0.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gitinspired = src.greetings_cli:main"
        ]
    },
    install_requires=[
        "argparse"
    ],
)
