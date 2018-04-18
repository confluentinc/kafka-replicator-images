import setuptools


setuptools.setup(
    name='kafka-connect-tests',
    version='0.0.1',

    author="Confluent, Inc.",
    author_email="partner-support@confluent.io",

    description='Docker image tests',

    url="https://github.com/confluentinc/kafka-connect-images",

    dependency_links=open("requirements.txt").read().split("\n"),

    packages=['test'],

    include_package_data=True,

    python_requires='>=2.7',
    setup_requires=['setuptools-git'],

)
