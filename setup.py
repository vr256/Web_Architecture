from setuptools import setup

setup(
    name='time_tracking',
    packages=['time_tracking'],
    include_package_data=True,
    install_requires=[
        'flask',
        'mysql-connector',
        'bcrypt',
    ],
)