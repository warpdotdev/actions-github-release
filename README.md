# GitHub Actions: Get Github release
This is a Warp-specific fork of rez0n/actions-github-release.

This Action able to get latest release version (tag) of the remote repository.

## Configuration

### Inputs

Name | Description | Example
--- | --- | ---
repository | The Github owner/repository | `nodejs/node`
channel | The release channel (prerelease or beta or stable) | `stable`
token | Github auth token (default variable for each aciton session) | `${{ secrets.GITHUB_TOKEN }}`

#### Possible values for `channel` input
* *stable* - Get the stable `latest` release
* *beta* - Get the beta `latest` release
* *dev* - Get the latest `dev`

### Outputs
Action outputs variable `release` with tag name of release.

## Usage example

```
on:
  push:
    branches: [ main ]

jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
    
    - name: Get latest release of NodeJS
      uses: rez0n/actions-github-release@main
      id: node_release
      env:
        token: ${{ secrets.GITHUB_TOKEN }}
        repository: "nodejs/node"
        channel: "stable"
        
    - name: Build image
      uses: docker/build-push-action@v1
        with:
          ...
          dockerfile: Dockerfile
          tags: latest, ${{ steps.node_release.outputs.release }}
```
