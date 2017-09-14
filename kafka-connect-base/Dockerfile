#
# Copyright 2016 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Builds a docker image for Kafka Connect

ARG DOCKER_REGISTRY
ARG DOCKER_TAG

# TODO: Get master branch images published, and use as a base.
# FROM ${DOCKER_REGISTRY}confluentinc/cp-kafka:master-latest
FROM ${DOCKER_REGISTRY}confluentinc/cp-kafka:${DOCKER_TAG}

ARG CONNECT_VERSION
ARG ARTIFACT_ID

# Hard-code component to override parent (ARG is ineffective)
ENV COMPONENT=kafka-connect

MAINTAINER partner-support@confluent.io
LABEL io.confluent.docker=true
ARG COMMIT_ID=unknown
LABEL io.confluent.docker.git.id=$COMMIT_ID
ARG BUILD_NUMBER=-1
LABEL io.confluent.docker.build.number=$BUILD_NUMBER

# Default kafka-connect rest.port
EXPOSE 8083

RUN echo "===> Setting up ${ARTIFACT_ID} dirs ..." \
    && mkdir -p /etc/${COMPONENT} /etc/${COMPONENT}/secrets /etc/${COMPONENT}/jars \
    && chmod -R ag+w /etc/${COMPONENT} /etc/${COMPONENT}/secrets /etc/${COMPONENT}/jars

# Install under "kafka-connect-images" to match CLASSPATH pattern used by connect startup scripts
ADD target/${ARTIFACT_ID}-${CONNECT_VERSION}-package/share/java/${ARTIFACT_ID}/* /usr/share/java/kafka-connect-images/

VOLUME ["/etc/${COMPONENT}/jars", "/etc/${COMPONENT}/secrets"]

COPY include/etc/confluent/docker /etc/confluent/docker

CMD ["/etc/confluent/docker/run"]
