#!/usr/bin/env groovy

docker_oraclejdk8 {
    dockerRepos = ['confluentinc/cp-kafka-connect-base', 'confluentinc/cp-kafka-connect', 'confluentinc/cp-enterprise-replicator']
    dockerRegistry = '368821881613.dkr.ecr.us-west-2.amazonaws.com/'
    dockerUpstreamRegistry = 'docker.io/'  // Temporary; use public images until new base images for trunk are published
    dockerUpstreamTag = 'latest'  // Temporary; use trunk-latest when available
    mvnPhase = 'integration-test'
    mvnSkipDeploy = true
    nodeLabel = 'docker-debian-jdk8-compose'
    withPush = true
}
