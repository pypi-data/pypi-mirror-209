from setuptools import setup

setup(
    name='shinherpro', 
    version='1.5.1',  
    description='TYAI Web Update Package',
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
)
