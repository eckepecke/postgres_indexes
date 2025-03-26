#!/bin/bash

# Ensure exactly 2 arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <HAMMERDB_VU> <HAMMERDB_WAREHOUSES>"
    exit 1
fi

# Assign arguments
# Hammer db recommends 2-4 VU per warehouse??
HAMMERDB_VU=$1
HAMMERDB_WAREHOUSES=$2

# Update existing .env file
sed -i.bak "s/^HAMMERDB_VU=.*/HAMMERDB_VU=$HAMMERDB_VU/" .env
sed -i.bak "s/^HAMMERDB_WAREHOUSES=.*/HAMMERDB_WAREHOUSES=$HAMMERDB_WAREHOUSES/" .env

echo "Updated .env file:"
cat .env

# Start containers in detached mode
docker-compose up -d

# Wait for PostgreSQL to become healthy
echo "Waiting for PostgreSQL to become ready..."
docker compose logs -f postgres | grep -q 'database system is ready to accept connections'

# Wait for HammerDB container to be fully initialized
echo "Waiting for HammerDB container to be ready..."
while ! docker inspect --format '{{.State.Running}}' exjobb-hammerdb 2>/dev/null | grep -q 'true'; do
    sleep 1
done

docker exec -it exjobb-hammerdb bash -c "./pg_tprocc_py.sh"
