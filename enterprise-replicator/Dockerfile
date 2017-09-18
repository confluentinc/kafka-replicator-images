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

ARG DOCKER_UPSTREAM_REGISTRY
ARG DOCKER_UPSTREAM_TAG

FROM ${DOCKER_UPSTREAM_REGISTRY}confluentinc/cp-kafka-connect-base:${DOCKER_UPSTREAM_TAG}

ARG CONNECT_VERSION
ARG ARTIFACT_ID

MAINTAINER partner-support@confluent.io
LABEL io.confluent.docker=true
ARG COMMIT_ID=unknown
LABEL io.confluent.docker.git.id=$COMMIT_ID
ARG BUILD_NUMBER=-1
LABEL io.confluent.docker.build.number=$BUILD_NUMBER

ADD target/${ARTIFACT_ID}-${CONNECT_VERSION}-package/share/doc/* /usr/share/doc/${ARTIFACT_ID}/

# Install under "kafka-connect-images" to match CLASSPATH pattern used by connect startup scripts
ADD target/${ARTIFACT_ID}-${CONNECT_VERSION}-package/share/java/${ARTIFACT_ID}/* /usr/share/java/kafka-connect-images/
