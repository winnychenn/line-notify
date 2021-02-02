#!/bin/bash

while :
do
  TEST=`date +"%M"`
  #python request.py
  echo $TEST
  if [ $TEST = "45" ] ;then
    python request.py  
  fi
  sleep 60s 
done

