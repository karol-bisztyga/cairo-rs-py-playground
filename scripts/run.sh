#!/bin/bash

set -e

# make sure you're not in the poetry shell or this script may not work

poetry run python src
