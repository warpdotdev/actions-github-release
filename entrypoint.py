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
        if release.body == "Warp Stable release":
            output.write('release={}\n'.format(release.tag_name))
            break
    elif wanted_release == 'beta':
        if release.body == "Warp Beta release":
            output.write('release={}\n'.format(release.tag_name))
            break
    elif wanted_release == 'canary':
        if release.body == "Nightly Warp Canary release":
            output.write('release={}\n'.format(release.tag_name))
            break
    elif wanted_release == 'preview':
        if release.body == "Nightly Warp Preview release":
            output.write('release={}\n'.format(release.tag_name))
            break
    elif wanted_release == 'dev':
        if release.body == "Nightly Warp Dev release":
            output.write('release={}\n'.format(release.tag_name))
            break
    else:
        print('Can\'t get release')
