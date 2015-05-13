Jenkins Docker Volume
=====================

WIP. :)

Usage
-----

1. Fork this repository.
2. Modify `plugins.yml` to contain the plugins you desire.
3. ???
4. Profit.
5. Launch your containers

    docker run --name jenkins-vol pitchplay/jenkins-vol
    docker run -p 8080:8080 --volumes-from jenkins-vol jenkins
