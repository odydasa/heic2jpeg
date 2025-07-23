from setuptools import setup, find_packages

setup(
    name="heic2jpeg",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pillow", "pillow-heif"],
    entry_points={
        "console_scripts": [
            "heic2jpeg=heic2jpeg.heic2jpeg:main"
        ]
    },
    include_package_data=True,
)
