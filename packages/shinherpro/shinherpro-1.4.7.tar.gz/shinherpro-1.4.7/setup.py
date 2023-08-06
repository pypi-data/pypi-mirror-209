from setuptools import setup

setup(
    name='shinherpro', 
    version='1.4.7',  
    description='shinher online system update',
    author='Yihuan', 
    author_email='ivan17.lai@gmail.com',  
    packages=['tyai'], 
    install_requires=[ 
        'selenium',
        'beautifulsoup4',
        'keras',
        'opencv-python',
        'Pillow',
        'tensorflow'
    ],
)
