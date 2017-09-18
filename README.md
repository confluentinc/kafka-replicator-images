# Docker images for Kafka Connect

This repo provides build files for [Kafka Connect](https://www.confluent.io/product/connectors/) Docker images.

We provide an ["All-In-One"](https://hub.docker.com/r/confluentinc/cp-kafka-connect/) image, which includes all connectors from [Confluent](https://www.confluent.io) OSS.

We also provide an image for [Enterprise Replicator](https://hub.docker.com/r/confluentinc/cp-enterprise-replicator/), part of Confluent Enterprise.

See [docs](docs/) for tutorials. For more on how to use Confluent's Docker images, see the [cp-docker-images documentation](http://docs.confluent.io/current/cp-docker-images/docs/index.html).


## Building

This project uses the `dockerfile-maven` plugin to build Docker images via Maven.

To build SNAPSHOT images, configure `.m2/settings.xml` for SNAPSHOT dependencies. These must be available at build time.

Pushing images to a registry is not currently part of the build.

```
mvn clean package  # Build local images
```

### Build Properties

- *docker.skip-build*: Set to `false` to include Docker images as part of build.
- *docker.skip-test*: Set to `false` to include Docker image integration tests as part of the build. Requires Python 2.7, `tox`.
- *docker.registry*: Build images for a private registry. Trailing `/` is required.
- *docker.tag*: Tag postfix for built images.
- *docker.upstream-registry*: Registry to pull base images and test dependency images from. Trailing `/` is required.
- *docker.upstream-tag*: Use the given tag postfix when pulling base images and test dependency images.


## Testing

Python 2.7 and `tox` are required for running tests.

```
mvn clean integration-test  # Build local images, and run Python integration tests
```
