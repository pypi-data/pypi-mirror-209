from setuptools import setup, find_packages


setup(
    name='flyem_segmentation_pipeline',
    version='1.3.3',
    license='MIT',
    author="Sai Harshavardhan Reddy Kona",
    author_email='s.kona001@umb.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/kshvr16/CS410_FlyEM_PyPi',
    description='A package based on traditional segmentation algorithms used to segment a fly retina images.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    project_urls={
        'Bug Tracker': 'https://github.com/kshvr16/CS410_FlyEM_PyPI/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'medical image',
        'medical image segmentation',
        'fly retina images',
        'electron microscopy images',
    ],
    install_requires=[
        'matplotlib',
        'scikit-image'
      ],

)
