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

ARG CONNECT_VERSION

FROM confluentinc/cp-kafka-connect-base:${CONNECT_VERSION}

ARG CONNECT_VERSION
ARG ARTIFACT_ID

MAINTAINER partner-support@confluent.io
LABEL io.confluent.docker=true
ARG COMMIT_ID=unknown
LABEL io.confluent.docker.git.id=$COMMIT_ID
ARG BUILD_NUMBER=-1
LABEL io.confluent.docker.build.number=$BUILD_NUMBER

# Default kafka-connect rest.port
EXPOSE 8083

RUN echo "===> Setting up ${ARTIFACT_ID} dirs ..." \
    && mkdir -p /etc/${ARTIFACT_ID} /etc/${ARTIFACT_ID}/secrets /etc/${ARTIFACT_ID}/jars \
    && chmod -R ag+w /etc/${ARTIFACT_ID} /etc/${ARTIFACT_ID}/secrets /etc/${ARTIFACT_ID}/jars

ADD target/${ARTIFACT_ID}-${CONNECT_VERSION}-package/share/java/${ARTIFACT_ID}/* /usr/share/java/${ARTIFACT_ID}/

VOLUME ["/etc/${ARTIFACT_ID}/jars", "/etc/${ARTIFACT_ID}/secrets"]

COPY include/etc/confluent/docker /etc/confluent/docker

CMD ["/etc/confluent/docker/run"]
