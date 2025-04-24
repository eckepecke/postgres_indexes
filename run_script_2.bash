#!/bin/bash

for i in {1..5}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpch.bash 20 1 ADD_INDEXES
done

for i in {1..3}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpch.bash 20 1 TPCC_STANDARD
done

for i in {1..5}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpch.bash 20 1 ADD_READ_HEAVY
done