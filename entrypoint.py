#!/usr/bin/env python3

from github import Github
import os
wanted_release = os.environ['channel']
repository = os.environ['repository']
token = os.getenv('token', None)

output = open(os.environ['GITHUB_OUTPUT'], 'a')

G = Github(token)
repo = G.get_repo(repository)
releases = repo.get_releases()
for release in releases:
    if wanted_release == 'stable':
        if "Stable release" in release.body:
            output.write('release={}\n'.format(release.tag_name))
            break
    elif wanted_release == 'beta':
        if "Beta release" in release.body:
            output.write('release={}\n'.format(release.tag_name))
            break
    elif wanted_release == 'canary':
        if "Canary release" in release.body:
            output.write('release={}\n'.format(release.tag_name))
            break
    elif wanted_release == 'preview':
        if "Preview release" in release.body:
            output.write('release={}\n'.format(release.tag_name))
            break
    elif wanted_release == 'dev':
        if "Dev release" in release.body:
            output.write('release={}\n'.format(release.tag_name))
            break
    else:
        print('Can\'t get release')
