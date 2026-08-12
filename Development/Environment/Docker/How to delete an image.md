How to delete an image

# How to delete an image
First get a list of all available images.
`Docker images`

|REPOSITORY|TAG|IMAGE ID|CREATED|SIZE|
|---|---|---|---|---|
|herbie68/development|buildregression|202279912e4f|57 minutes ago|908MB|
|buildregression|latest|202279912e4f|57 minutes ago |908MB|
|herbie68/buildregression|latest|202279912e4f|57 minutes ago|908MB|
|herbie68/development/buildregression|latest|202279912e4f|57 minutes ago|908MB|
|docker101tutorial|latest|5ccd92400052|3 hours ago|27.3MB|
|nginx|alpine|6f715d38cfe0|4 days ago|22.1MB|
|python|3.8|79cc46abd78d|6 days ago|882MB|
|python|latest|79cc46abd78d|6 days ago|882MB|

An image can be deleted using its:
- Repository   (if no tag is used)
- Repository:tag
- Tag
- Image ID

## Commands
`Docker rmi <repository>`

`Docker rmi <repository:tag>`

`Docker rmi <tag>`

`Docker rmi <id>`