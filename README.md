<p align="center">
  <img src=".asset/magiceyeGit.png" width="350" title="hover text">
  <br>
  <br>
  <a href=https://github.com/Sir-Thom><img src="https://img.shields.io/badge/Lead Dev-Thomas Toulouse-blue"></a>
  <img src="https://img.shields.io/badge/Os-Linux-brightgreen">
  <a href=https://github.com/Sir-Thom/Magic-Eye/releases/tag/v0.80><img src="https://img.shields.io/badge/Version-0.80-informational"></a>
  <img src="https://img.shields.io/badge/tested with -Raspberry pi 3 64 bit-sucess">
</p>
<br>
<h3 align="center">
<p>This small gui application let you stream a live video to a other computer. </p>
</h3>
<br>

# Note the futur main branch will be base on Rework-Tauri
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSir-Thom%2FMagic-eye.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FSir-Thom%2FMagic-eye?ref=badge_shield)


# Note for running the backend
here what you need to run the backend of this application.
## Docker
to build the docker image run the following command:
```
docker build -t nginx_hls_converter .
docker run -it -p 127.0.0.1:8080:80 -p 127.0.0.1:1935:1935 --name nginx_hls nginx_hls_converter
```
for the backend that will deal with rtmp you can use this repo:
https://github.com/Sir-Thom/rtmpserverMagic-eye

after that you can use the following command to stream a video to the server:
```
git clone https://github.com/Sir-Thom/rtmpserverMagic-eye.git
cd rtmpserverMagic-eye
cargo run 
```

## Table of Contents
- [Note the futur main branch will be base on Rework-Tauri](#note-the-futur-main-branch-will-be-base-on-rework-tauri)
- [Note for running the backend](#note-for-running-the-backend)
  - [Docker](#docker)
  - [Table of Contents](#table-of-contents)
  - [Dependancies](#dependancies)
  - [Installation](#installation)
  - [Uninstall](#uninstall)
  - [Update](#update)
  - [Patterns](#patterns)


## Dependancies
```
python3
gtk3
gstreamer
gst-plugins-bad
gst-plugins-base
gst-plugins-good
gst-plugins-openh264
gst-plugins-ugly
gst-rtsp-server
pyinstaller
pip3
```
if pyinstaller is not in your distribution repository
you can install it with this command  **note: execute them whit sudo**
```
pip install -U pyinstaller
```
## Installation
for x86_64 architecture
```
git clone https://github.com/Thomas-Toulouse/Magic-Eye.git
cd Magic-Eye
make
```
for ARM_64 architecture
```
git clone https://github.com/Thomas-Toulouse/Magic-Eye.git
cd Magic-Eye
make installArm
```
## Uninstall
```
cd Magic-Eye
make uninstall
```
## Update
for x86_64 architecture
```
cd Magic-Eye
make update
```
for ARM_64 architecture
```
cd Magic-Eye
make updateArm
```
## Patterns

| Patterns                                                                                            |  config arguments                                          |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <img src="/.asset/pattern/Preview_Magic_Eye_Client.png" width="120" heigth=120>                     |<p align="center">smpte-rp-219</p>                          |
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_smpte.png" width="120" heigth=120>               |<p align="center">smpte</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_snow.png" width="120" heigth=120>                |<p align="center">snow</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_black.png" width="120" heigth=120>               |<p align="center">black</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_red.png" width="120" heigth=120>                 |<p align="center">red</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_blue.png" width="120" heigth=120>                |<p align="center">blue</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_green.png" width="120" heigth=120>               |<p align="center">green</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_checker1.png" width="120" heigth=120>            |<p align="center">checkers-1</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_checker2.png" width="120" heigth=120>            |<p align="center">checkers-2</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_checker4.png" width="120" heigth=120>            |<p align="center">checkers-4</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_checker8.png" width="120" heigth=120>            |<p align="center">checkers-8</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_circular.png" width="120" heigth=120>            |<p align="center">circular</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_smpte75.png" width="120" heigth=120>             |<p align="center">smpte75</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_zoneplate.png" width="120" heigth=120>           |<p align="center">zone-plate kx2=20 ky2=20 kt=1</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_gamut.png" width="120" heigth=120>               |<p align="center">gamut</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_chromazoneplate.png" width="120" heigth=120>     |<p align="center">chroma-zone-plate kx2=20 ky2=20 kt=1</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_solidcolor.png" width="120" heigth=120>          |<p align="center">solid-color</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_ball.png" width="120" heigth=120>                |<p align="center">ball</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_smpte100.png" width="120" heigth=120>            |<p align="center">smpte100</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_bar.png" width="120" heigth=120>                 |<p align="center">bar</p>
| <img src="/.asset/pattern/Preview-Magic_Eye_Client_pinwheel.png" width="120" heigth=120>            |<p align="center">pinwheel</p>
| <img src="/.asset/pattern/Preview_Magic_Eye_Client_spokes.png" width="120" heigth=120>              |<p align="center">spokes</p>
| <img src="/.asset/pattern/Preview_Magic_Eye_Client_gradient.png" width="120" heigth=120>            |<p align="center">gradient</p>
| <img src="/.asset/pattern/Preview_Magic_Eye_Client_color.png" width="120" heigth=120>               |<p align="center">colors</p>



## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSir-Thom%2FMagic-eye.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSir-Thom%2FMagic-eye?ref=badge_large)