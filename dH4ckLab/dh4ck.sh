IMAGE=dh4ck_lab
CONTAINER=dh4ck
function dh4ck_up() {
  local wpath="$1"
  local volume=""

  # Setting volume if path was specified
  if [[ ! -z "${wpath}" ]]; then 
    if [ ! -d "${wpath}" ]; then
      echo "Unknown path: cannot mount directory as volume"
      return
    fi
    volume="-v ${wpath}:/home/qh4ck/host_data"
    # Remove the container to reset volume
    docker stop ${CONTAINER} > /dev/null 2>&1;
    docker rm ${CONTAINER} > /dev/null 2>&1;
  fi

  # Check if image exists
  if [ ! "$(docker images | grep ${IMAGE})" ]; then
    docker build -t dh4ck_lab . # TODO: add image to docker hub
  fi
  # Check if container exist
  if [ ! "$(docker ps -a | grep ${CONTAINER})" ]; then
    docker run ${volume} -id --name ${CONTAINER} ${IMAGE}
  else
    # If stopped restart
    if [ ! "$(docker ps | grep ${CONTAINER})" ]; then
      docker start ${CONTAINER}
    fi
  fi
  # Executing bash
  docker exec -i -t ${CONTAINER} /bin/bash
}

function dh4ck() {
  local wpath=""
  local stopcontainer=false
  local removecontainer=false
  local removeimage=false
  local help_string="Arguments:
  no_options:    open the lab
  -l, --lclean:  stop the container
  -c, --clean:   stop and remove the container
  -r, --remove:  remove the image
  -h, --help:    display options
  "

  # If no arguments run the lab otherwise, if a path is provided
  # Parse the path and run the lab mounting the volume
  if [ $# -eq 0 ]; then
    dh4ck_up; return
  elif [[ "$1" == *'/'* ]]; then
    # Parsing user argument as path
    if [[ "$1" == '/'* ]]; then 
      wpath="$1"
    else 
      wpath="$(pwd)/$1"
    fi
    dh4ck_up "${wpath}"; return
  fi

  # Collecting arguments
  while (( "$#" )); do 
    case $1 in
      -l|--lclean)
        stopcontainer=true;;
      -c|--clean) 
        stopcontainer=true
        removecontainer=true;;
      -r|--remove) 
        stopcontainer=true
        removecontainer=true
        removeimage=true;;
      -h|--help)
        echo "$help_string"
        return;;
      *)
        echo "Unknown argument: $1"
        echo "$help_string"
        return;;
    esac; 
    shift
  done

  # Acting
  if [ "$stopcontainer" = true ]; then
    echo "Stopping container..."; docker stop ${CONTAINER} > /dev/null 2>&1;
  fi
  if [ "$removecontainer" = true ]; then
    echo "Removing container..."; docker rm ${CONTAINER} > /dev/null 2>&1;
  fi
  if [ "$removeimage" = true ]; then
    echo "Deleting image..."; docker rmi ${IMAGE} > /dev/null 2>&1;
  fi
}

