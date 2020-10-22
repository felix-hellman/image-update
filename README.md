
# image-update
Drone plugin to update image tag in deployment yaml files for kubernetes.
Primarily to be used in conjuction with argo.

## Example usage 
Update build image from previous version to current version based on commit hash (8 characters)

```yaml
kind: pipeline
type: docker
name: default

steps:
- name: update-tag-yaml
  image: docker.pkg.github.com/felix-hellman/image-update/image-update:0.2
  commands:
    - python3 /drone/imageupdate.py path/to/deployment.yaml ${DRONE_COMMIT_SHA:0:8}
```
