# GitHub Actions: Get Github release
This Action able to get latest release version (tag) of the remote repository.

## Configuration

### Inputs

Name | Description | Example
--- | --- | ---
repository | The Github owner/repository | `nodejs/node`
type | The release type (prerelease or beta or stable) | `stable`
token | Github auth token (default variable for each aciton session) | `${{ secrets.GITHUB_TOKEN }}`

#### Possible values for `type` input
* *stable* - Get the stable `latest` release
* *beta* - Get the beta `latest` release
* *prerelease* - Get the latest `prerelease` (i.e. what we refer to as dev)
* *latest* - Get the *really* latest release with no matter what the channel version is

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
        type: "stable"
        
    - name: Build image
      uses: docker/build-push-action@v1
        with:
          ...
          dockerfile: Dockerfile
          tags: latest, ${{ steps.node_release.outputs.release }}
```
