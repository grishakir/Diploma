#!/bin/bash

# Start Xvfb
Xvfb :99 -screen 0 1024x768x16 &

# Execute the command passed to the container
exec "$@"