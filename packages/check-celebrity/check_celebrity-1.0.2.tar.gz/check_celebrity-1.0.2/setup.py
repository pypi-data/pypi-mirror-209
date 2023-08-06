from setuptools import setup

setup(
    name='check_celebrity',
    version='1.0.2',
    description='Celebrity check Package',
    packages=['check_celebrity'],
    install_requires=[
        'Deepface',
        'mtcnn',
        'VGGFace',
        'keras',
        'Tensorflow',
        'numpy',
        'opencv-python',
        'Flask',
        'Pillow==9.5.0'
    ],
)