#!/bin/bash

source /tmp/createprimary.sh
source /tmp/createstandby.sh

if [ $NODE = "primarydb" ]; then
  StartPrimary
else
  StartStandby
fi