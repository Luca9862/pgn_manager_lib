from setuptools import setup

setup(
    name="pgn_manager",
    version="1.2.7",
    description="library for managing pgn files",
    author="Luca Canali",
    author_email="lucacanali.dev@gmail.com",
    packages= ["pgn_manager"],
    install_requires=[
        "python-chess",
    ],
)