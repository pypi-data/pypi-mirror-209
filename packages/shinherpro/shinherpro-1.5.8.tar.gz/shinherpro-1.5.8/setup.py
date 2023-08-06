from setuptools import setup
from setuptools.command.install import install

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

class CustomInstallCommand(install):
    def run(self):
        print("\033[93m 正在安裝shinher-pro...")
        install.run(self)
        print("shinherpro安裝完成！ \033[0m")

setup(
    name='shinherpro',
    version='1.5.8',
    description='shinher-pro 1.5.8',
    author='Yihuan',
    author_email='ivan17.lai@gmail.com',
    packages=['shinherpro'],
    install_requires=[
        'selenium',
        'beautifulsoup4',
        'keras',
        'opencv-python',
        'Pillow',
        'tensorflow'
    ],
    long_description=readme,
    long_description_content_type='text/markdown',
    cmdclass={
        'install': CustomInstallCommand,
    }
)
