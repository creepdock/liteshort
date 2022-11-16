import setuptools

setuptools.setup(
    name="liteshort",
    version="1.2.3",
    author="Rose Spangler",
    author_email="132@ikl.sh",
    description="User-friendly, actually lightweight, and configurable URL shortener",
    url="https://git.ikl.sh/132ikl/liteshort",
    packages=setuptools.find_packages(),
    package_data={"liteshort": ["templates/*", "static/*", "config.template.yml"]},
    entry_points={
        "console_scripts": [
            "liteshort = liteshort.main:app.run",
            "lshash = liteshort.util:hash_passwd",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=["flask", "bcrypt", "pyyaml", "appdirs", "requests"],
    python_requires=">=3.8",
)
