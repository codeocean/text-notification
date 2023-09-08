#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    set_log_msg "No arguments supplied" --log-level "info"
else
    set_log_msg "$*" --log-level "info"
fi


if [ -z "$1" ]; then
  phone="0"
else
  phone="$1"
fi

if [ -z "$2" ]; then
  notification="Code Ocean text notification capsule"
else
  notification="$2"
fi

if [ -z "$3" ]; then
  export CO_LOG="false"
else
  if [ "$3" = "on" ]; then
    export CO_LOG="true"
  else
    export CO_LOG="false"
  fi
fi

if [ -z "$4" ]; then
  export CO_LOG_LEVEL="WARNING"
else
  if [ "$4" = "debug" ]; then
    export CO_LOG_LEVEL="debug"
  elif [ $3 = "info" ]; then
    export CO_LOG_LEVEL="info"
  elif [ $3 = "warning" ]; then
    export CO_LOG_LEVEL="warning"
  elif [ $3 = "error" ]; then
    export CO_LOG_LEVEL="error"
  elif [ $3 = "critical" ]; then
    export CO_LOG_LEVEL="critical"
  else
    export CO_LOG_LEVEL="WARNING"
  fi
fi