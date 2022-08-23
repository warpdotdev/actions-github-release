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
        if release.body == "Warp Stable release":
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'beta':
        if release.body == "Warp Beta release":
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'canary':
        if release.body == "Nightly Warp Canary release":
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'preview':
        if release.body == "Nightly Warp Preview release":
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'dev':
        if release.body == "Nightly Warp Dev release":
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    else:
        print('Can\'t get release')
