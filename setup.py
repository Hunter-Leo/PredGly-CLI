from setuptools import setup, find_packages

setup(
    name="predgly",
    version="1.0.0",
    description="PredGly: Predicting lysine glycation sites for homo sapiens",
    author="PredGly Team",
    py_modules=["cli"],
    include_package_data=True,
    package_data={
        '': ['codes/*'],
    },
    entry_points={
        'console_scripts': [
            'predgly=cli:main',
        ],
    },
    install_requires=[
        'numpy',
        'pandas', 
        'matplotlib',
        'scipy',
        'scikit-learn',
    ],
    python_requires='>=2.7,<3',
)
