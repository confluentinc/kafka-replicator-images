import setuptools


setuptools.setup(
    name='kafka-replicator-tests',
    version='0.0.1',
    author="Confluent, Inc.",
    author_email="replicator@confluent.io",
    description='Kafka Replicator docker image tests',
    url="https://github.com/confluentinc/kafka-connect-images",
    dependency_links=open("requirements.txt").read().split("\n"),
    packages=['test'],
    include_package_data=True,
    python_requires='>=2.7',
    setup_requires=['setuptools-git'],
)
