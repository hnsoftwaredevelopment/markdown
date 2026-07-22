Windows based containers on docker

# Windows based containers on docker
[TOC]

## Source
[Python 3.8.5 on docker hub](https://hub.docker.com/_/python?tab=tags&page=1&name=3.8.5-w)

## Full version container
|---|---|
|IMAGE|3.8.5-windowsservercore-ltsc2016|
|Command|docker pull python:3.8.5-windowsservercore-ltsc2016|


|DIGEST|OS/ARCH|COMPRESSED SIZE|
|---|---|---:|
|f9943ee7b873|windows/amd64|5.41 GB|

Steps I executed
- docker pull python:3.8.5-windowsservercore-ltsc2016
- docker tag python:3.8.5-windowsservercore-ltsc2016 herbie68/development:python385-winsvr2016
- docker push herbie68/development:python385-winsvr2016

## Compressed version container
|---|---|
|IMAGE|3.8.5-windowsservercore-1809|
|Command|docker pull python:3.8.5-windowsservercore-1809|


|DIGEST|OS/ARCH|COMPRESSED SIZE|
|---|---|---:|
|98d516774083|windows/amd64|2.24 GB|

Steps I executed
- docker pull python:3.8.5-windowsservercore-1809
- docker tag python:3.8.5-windowsservercore-1809 herbie68/development:python385-winsvr2016-1809
- docker push herbie68/development:python385-winsvr2016-1809