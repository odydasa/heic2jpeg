from setuptools import setup, find_packages

setup(
    name='heic2jpeg',
    version='1.0.0',
    description='Convert .heic images to .jpg format via CLI or GUI.',
    author='OdyDasa',
    author_email='you@example.com',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[
        'pillow',
        'pillow-heif'
    ],
    entry_points={
        'console_scripts': [
            'heic2jpeg=heic2jpeg:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
