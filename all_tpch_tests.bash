#!/bin/bash

for i in {1..6}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpch.bash 1 1 TPCH_STANDARD
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpch.bash 1 1 ADD_INDEXES
done

for i in {1..10}; do
    echo "Run #$i"
    docker compose down -v

    # Wait until no containers are running or existing
    while [ "$(docker ps -aq)" ]; do
        echo "Waiting for all containers to be removed..."
        sleep 1
    done

    ./execution_script_tpch.bash 1 1 ADD_USEFUL
done
