How to publish a Docker image to the repo

# How to publish a Docker image to the repo

## Prereguisits
|---|---|
|Docker user|herbie68|
|Repository |development|

## Steps
- Build the image `Docker build -t <imagename> .`
- Re-tag the image using prerequisites `Docker tag <imagename> herbie68/development:<imagename>`
- Push the image `Docker push herbie68/development:<imagename>`

Step on an two could be combined in the build step using the credentials in the tag `Docker build -t herbie68/development:<imagename> .`