#!/usr/bin/env groovy

dockerfile {
    dockerPush = false
    dockerRepos = ['confluentinc/cp-enterprise-replicator',
      'confluentinc/cp-enterprise-replicator-executable']
    mvnPhase = 'package'
    mvnSkipDeploy = true
    nodeLabel = 'docker-oraclejdk8-compose-swarm'
    slackChannel = 'tools-notifications' //TODO: change to correct team
    upstreamProjects = [] //TODO: after roll out update
    dockerPullDeps = ['confluentinc/cp-base-new', 'confluentinc/cp-server-connect-base']
    usePackages = true
    cron = '' // Disable the cron because this job requires parameters
}
