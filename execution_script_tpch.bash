#!/bin/bash

# Ensure exactly 3 arguments are passed
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <HAMMERDB_VU> <HAMMERDB_SCALE_FACTOR> <INDEX_SETTING>"
    echo "Possible settings:"
    echo "1. DROP"
    echo "2. TPCC_STANDARD"
    echo "3. MORE_MULTI_COLUMN"
    exit 1
fi

# Assign arguments
# Hammer db recommends 2-4 VU per warehouse??
HAMMERDB_VU=$1
HAMMERDB_SCALE_FACTOR=$2
INDEX_SETTING=$3

# Update existing .env file
cat > .env <<EOF
HAMMERDB_VU=$HAMMERDB_VU
HAMMERDB_SCALE_FACTOR=$HAMMERDB_SCALE_FACTOR
EOF
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

docker exec -it exjobb-hammerdb bash -c "./pg_tproch_py_${INDEX_SETTING}.sh"
