#!/usr/bin/env groovy

dockerfile {
    dockerRepos = ['confluentinc/cp-kafka-connect-base', 'confluentinc/cp-kafka-connect', 'confluentinc/cp-enterprise-replicator']
    dockerPullDeps = ['confluentinc/cp-kafka']
    dockerRegistry = '368821881613.dkr.ecr.us-west-2.amazonaws.com/'
    dockerUpstreamTag = '4.1.x-71'
    mvnPhase = 'package'
    mvnSkipDeploy = true
    nodeLabel = 'docker-oraclejdk8-compose'
    dockerPush = true
    slackChannel = '#connect-eng'
}
