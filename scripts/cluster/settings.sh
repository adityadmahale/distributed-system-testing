#!/bin/bash

PGDATA=/tmp/my_data
AUTH=trust

if [ "$DATABASE_TYPE" = "epas" ]; then
  PGENGINE=/usr/edb/as${DATABASE_VERSION}/bin
else
  PGENGINE=/usr/pgsql-${DATABASE_VERSION}/bin
fi
