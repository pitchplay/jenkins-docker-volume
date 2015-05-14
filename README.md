Jenkins Docker Volume
=====================

[![Build Status](https://travis-ci.org/pitchplay/jenkins-docker-volume.svg)](https://travis-ci.org/pitchplay/jenkins-docker-volume)

WIP. :)

The motiviation behind this is to have the ability to deploy jenkins into a
stateless environment such as [mesos](https://mesos.apache.org/) using docker,
but pre-configured with all the plugins and jobs needed to work out of the box.
This enables the ability for the jenkins master to fail and be rebalanced in a
clustered environment, without needing to worry about persistances.

There are some cons to this approach:

  * If you're particularly concerned about maintaining a build history
  for audit compliance purposes, this will not work for you.
  * Jenkins built-in artifact store becomes unreliable. (Should look into 
  using something like [artifactory](http://www.jfrog.com/open-source/#os-arti)

Usage
-----

1. Fork this repository.
2. Modify `plugins.yml` to contain the plugins you desire.
3. ???
4. Profit.
5. Launch your containers

Testing
-------

Just run:

    docker-compose up

Now navigate to [localhost:8080](http://localhost:8080).
