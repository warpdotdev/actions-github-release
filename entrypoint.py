#!/usr/bin/env python3

from github import Github
import os
wanted_release = os.environ['channel']
repository = os.environ['repository']
token = os.getenv('token', None)

G = Github(token)
repo = G.get_repo(repository)
releases = repo.get_releases()
for release in releases:
    if wanted_release == 'stable':
        if release.prerelease == 0 and release.draft == 0 and release.body == "Warp Stable release":
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'beta':
        if release.prerelease == 0 and release.draft == 0 and release.body == "Warp Beta release":
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'prerelease':
        if release.prerelease == 1:
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'latest':
        print('::set-output name=release::{}'.format(release.tag_name))
        break
    else:
        print('Cant get release')
