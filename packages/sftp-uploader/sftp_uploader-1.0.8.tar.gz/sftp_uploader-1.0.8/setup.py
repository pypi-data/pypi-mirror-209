from setuptools import setup, find_packages
from setuptools.command.install import install

from sftp_uploader.post_install import add_config_file_to_gitignore, add_sftp_upload_in_prehook


class PostInstallClass(install):
    def run(self):
        """
            Actions after installing package
        """
        print('sex')
        install.run(self)
        print('sex2')
        add_config_file_to_gitignore()
        add_sftp_upload_in_prehook()


setup (
    name='sftp_uploader',
    version='1.0.8',
    description='Package for upload data to sftp with different parametrs and with different methods',
    author='Moonvent',
    license='MIT',
    packages=find_packages(),

    # install_requires=[
    #     # 'dependency1',
    #     # 'dependency2',
    # ],

    cmdclass = {'install': PostInstallClass}

    # scripts=[
    #     'post_install.py',
    # ],
)
