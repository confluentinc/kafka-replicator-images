#!/usr/bin/env groovy

dockerfile {
    dockerPush = true
    dockerRepos = ['confluentinc/cp-enterprise-replicator',
      'confluentinc/cp-enterprise-replicator-executable']
    mvnPhase = 'package'
    mvnSkipDeploy = true
    nodeLabel = 'docker-debian-jdk8-compose'
    slackChannel = '#replicator-alerts'
    upstreamProjects = []
    dockerPullDeps = ['confluentinc/cp-base-new', 'confluentinc/cp-server-connect-base']
    usePackages = true
    cron = '' // Disable the cron because this job requires parameters
    cpImages = true
    osTypes = ['ubi8']
    nanoVersion = true
    buildArm = true
}
