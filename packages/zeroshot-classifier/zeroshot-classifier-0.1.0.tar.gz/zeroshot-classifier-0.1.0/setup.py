from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = """
code and data for the Findings of ACL'23 paper Label Agnostic Pre-training for Zero-shot Text Classification 
by Christopher Clarke, Yuzhao Heng, Yiping Kang, Krisztian Flautner, Lingjia Tang and Jason Mars
 """

setup(
    name='zeroshot-classifier',
    version=VERSION,
    license='MIT',
    author='Christopher Clarke & Yuzhao Heng',
    author_email='csclarke@umich.edu',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url='https://github.com/ChrisIsKing/zero-shot-text-classification',
    download_url='https://github.com/ChrisIsKing/zero-shot-text-classification/archive/refs/tags/v0.1.0.tar.gz',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'gdown', 'openai', 'requests', 'tenacity',
        'spacy', 'nltk', 'scikit-learn', 'torch', 'sentence-transformers', 'transformers',
        'datasets',
        'stefutils'
    ],
    keywords=['python', 'nlp', 'machine-learning', 'deep-learning', 'text-classification', 'zero-shot-classification'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: GPU :: NVIDIA CUDA',
        'Environment :: GPU :: NVIDIA CUDA :: 11.6',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Visualization'
    ]
)
