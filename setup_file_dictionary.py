from setuptools import setup

setup(
    name="merriam-webster-cli",
    version="1.0",
    packages=["merriam_webster_cli"],
    install_requires=["requests", "argparse"],
    entry_points={
        "console_scripts": ["merriam-webster-cli=merriam_webster_cli.main:main"]
    }
)
