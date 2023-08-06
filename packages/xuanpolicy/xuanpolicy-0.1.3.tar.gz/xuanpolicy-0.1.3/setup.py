from setuptools import find_packages, setup

setup(
    name='xuanpolicy',
    packages=find_packages(include=['xuanpolicy', 'xuanpolicy.*']),
    package_data={"xuanpolicy": ["configs/*.yaml", "configs/*/*/*.yaml"]},
    version='0.1.3',
    description='Deep reinforcement learning library.',
    author='Wenzhang Liu, Wenzhe Cai, Kun Jiang, etc.',
    author_email='',
    license='MIT',
    url='',
    download_url='',
    keywords=['deep reinforcement learning', 'software library', 'platform'],
    classifiers=[
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.6',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
    test_suite='tests',
)
