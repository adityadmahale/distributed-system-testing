#!/bin/bash

StartDBServer () {
  sudo -H -u $DATABASE_USER bash -c "$PGENGINE/pg_ctl -o \"-p $DBPORT\" -D $PGDATA start -w"
}

WaitForExit(){
  while true; do
     sleep 30
  done
}
