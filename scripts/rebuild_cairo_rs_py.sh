#!/bin/bash

set -e

# make sure you're not in the poetry shell or this script may not work

echo "rebuilding cairo-rs-py..."

poetry remove cairo-rs-py || echo "cairo-rs-py not found, skipping removing..."
poetry add ./cairo-rs-py


echo "REBUILT"