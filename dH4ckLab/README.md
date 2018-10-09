# dH4ckLab
A simple container collecting all basic tools needed to play CTFs.
## Installation
Once you've download the repo, enter the directory and run:
```
$ source dh4cklab.sh
```
This will enable the basic command to run and remove the container
### Commands
To open a shell inside the container run:
```
$ dh4ck <path>
```
The image will be built and the container run, if necessary. If path is specified the directory will be mounted as a volume under "/home/qh4ck/host_data", otherwise no volume will be provided by default.
The command can be run with the following arguments:
```
$ dh4ck -h
Arguments:
  no_options:   open the lab
  -s, --clean:  stop the container
  -l, --lclean: stop and remove the container
  -s, --clean:  remove the image
  -h, --help:   display options
```
