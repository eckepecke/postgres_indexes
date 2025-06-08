#!/bin/bash
# Large dataset

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 50 200 TPCC_STANDARD
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 50 200 ADD_INDEXES
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 50 200 ADD_READ_HEAVY
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 50 200 DROP_INDEXES
done

# Medium dataset

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 20 80 TPCC_STANDARD
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 20 80 ADD_INDEXES
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 20 80 ADD_READ_HEAVY
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 20 80 DROP_INDEXES
done

# Small dataset


for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 8 32 TPCC_STANDARD
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 8 32 ADD_INDEXES
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 8 32 ADD_READ_HEAVY
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpcc.bash 8 32 DROP_INDEXES
done