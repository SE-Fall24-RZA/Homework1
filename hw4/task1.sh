#!/bin/bash
 

PID=$(pgrep -f infinite.sh)

if [ ! -z "$PID" ]; then
  echo "Killing process with PID: $PID"
  kill $PID
  echo "Process killed."
else
  echo "No process found for infinite.sh"
fi


