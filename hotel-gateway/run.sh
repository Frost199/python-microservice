#!/bin/bash

until nc -z "${RABBIT_HOST}" "${RABBIT_PORT}"; do
    echo "$(date) - instantiating rabbitmq..."
    sleep 1
done

nameko run --config config.yml gateway
