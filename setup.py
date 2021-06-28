from setuptools import setup, find_packages

setup(
    name='taming-transformers-rom1504',
    version='0.0.3',
    description='Taming Transformers for High-Resolution Image Synthesis',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'numpy',
        'tqdm',
        'omegaconf>=2.0.0',
        'pytorch-lightning>=1.0.8'
    ],
)
