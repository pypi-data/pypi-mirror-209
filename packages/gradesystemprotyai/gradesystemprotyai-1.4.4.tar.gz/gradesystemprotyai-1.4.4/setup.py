from setuptools import setup

setup(
    name='gradesystemprotyai', 
    version='1.4.4',  
    description='TYAI Web Update Package',
    author='Yihuan', 
    author_email='ivan17.lai@gmail.com',  
    packages=['gradesystemprotyai'], 
    install_requires=[ 
        'selenium',
        'beautifulsoup4',
        'keras',
        'opencv-python',
        'Pillow',
        'tensorflow'
    ],
)
