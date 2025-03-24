from setuptools import setup

setup (
    name="cli",
    version="0.1.0",
    description="a simple CLI app to manage tasks",
    author="Serine",
    author_email="serineboukerroucha@gmail.com",
    py_modules=["cli"],
    entry_points={
        "console_script": [
            "cli=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS independent",
    ],
    python_requires=">=3.6"
)
