from setuptools import setup, find_packages

setup (
    name='sftp_uploader',
    version='1.0.7',
    description='Package for upload data to sftp with different parametrs and with different methods',
    author='Moonvent',
    license='MIT',
    packages=find_packages(),

    install_requires=[
        # 'dependency1',
        # 'dependency2',
    ],

    scripts=[
        'post_install.py',
    ],
)
