#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scaffold jenkins plugins for use in docker volume.

Downloads jenkins plugins based on supplied yaml configuration.
Requires:
    - pyyaml
"""

import logging
import shutil
from urllib.request import urlopen
import yaml

# Initialize Logging
logging.basicConfig(level=logging.DEBUG)


def _plugin_url(name, version):
    """
    Given a name and an optional version, return the jenkins plugin url.
    If there is no version, grab the latest version of the plugin.

    >>> _plugin_url("git", None)
    'https://updates.jenkins-ci.org/latest/git.hpi'
    >>> _plugin_url("git", "2.3.5")
    'https://updates.jenkins-ci.org/download/plugins/git/2.3.5/git.hpi'
    """
    uri = "latest" if version is None else "download/plugins"
    path = name if version is None else "{}/{}/{}".format(name, version, name)
    plugin = "/{}.hpi".format(path)
    return "https://updates.jenkins-ci.org/{}{}".format(uri, plugin)


def _parse_version(raw):
    """
    Given a colon delimited plugin string, parse a (name, version) tuple.

    >>> _parse_version("git:2.3.5")
    ('git', '2.3.5')
    >>> _parse_version("git")
    ('git', None)
    """
    tmp = raw.split(':')
    name = tmp[0]
    version = None if len(tmp) == 1 else tmp[1]
    return (name, version)


def fetch_plugin(name, version):
    """Download Jenkins plugin .hpi from update server"""
    url = _plugin_url(name, version)
    logging.info("Downloading {}: {}".format(name, url))
    with urlopen(url) as response, open("{}.hpi".format(name), 'wb') as outfile:
        shutil.copyfileobj(response, outfile)


def parse_plugin_yaml(yamlfile):
    """
    Parse given YAML file and return a list of key/value tuples.

    >>> demo_yaml_1 = '''
    ... plugins:
    ...   - git
    ... '''
    >>> demo_yaml_2 = '''
    ... plugins:
    ...   - git:2.3.5
    ... '''
    >>> parse_plugin_yaml(demo_yaml_1)
    [('git', None)]
    >>> parse_plugin_yaml(demo_yaml_2)
    [('git', '2.3.5')]
    """
    raw = yaml.load(yamlfile)
    plugin_list = raw.get('plugins')
    return [_parse_version(plugin) for plugin in plugin_list]


def main():
    """ Task Runner """
    yamlfile = open('plugins.yml', 'r')
    plugins = parse_plugin_yaml(yamlfile)
    for (plugin, version) in plugins:
        fetch_plugin(plugin, version)


if __name__ == '__main__':
    main()
