from setuptools import setup
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        print("\033[93m 正在安裝shinher-pro...")
        install.run(self)
        print("shinherpro安裝完成！ \033[0m")

setup(
    name='shinherpro', 
    version='1.5.5',  
    description='shinher-pro 1.5.5',
    author='Yihuan', 
    author_email='ivan17.lai@gmail.com',  
    packages=['shinherpro'], 
    data_files=[('shinherpro', ['vfc_AiModel_5.1_VGG16_black.h5'])],
    install_requires=[ 
        'selenium',
        'beautifulsoup4',
        'keras',
        'opencv-python',
        'Pillow',
        'tensorflow'
    ],
)
