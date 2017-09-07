# Docker images for Kafka Connect

This repo provides build files for [Kafka Connect](https://www.confluent.io/product/connectors/) Docker images.

We provide an ["All-In-One"](https://hub.docker.com/r/confluentinc/cp-kafka-connect/) image, which includes all connectors from [Confluent](https://www.confluent.io) OSS.

We also provide an image for [Enterprise Replicator](https://hub.docker.com/r/confluentinc/cp-enterprise-replicator/), part of Confluent Enterprise.

See [docs](docs/) for tutorials. For more on how to use Confluent's Docker images, see the [cp-docker-images documentation](http://docs.confluent.io/current/cp-docker-images/docs/index.html).

## Building

This project uses the `dockerfile-maven` plugin to build Docker images via Maven.

To build SNAPSHOT images, configure `.m2/settings.xml` for SNAPSHOT dependencies. These must be available at build time.

Pushing images is currently handled via `docker push`, and is not part of the build.

```
mvn clean package  # Build local images

# Build images for a private registry; trailing '/' is required:
# mvn package -Ddocker.registry=docker.example.com:8080/ -Ddocker.tag=$VERSION-$BUILD_NUMBER
```
