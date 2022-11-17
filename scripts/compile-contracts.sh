#!/bin/bash

set -e

# make sure you're not in the poetry shell or this script may not work

echo "compiling new..."

pushd starknet_0_10_1
poetry run starknet-compile ../contracts/simple-new.cairo --output ../compiled-contracts/simple-new.json
poetry run starknet-compile ../contracts/account.cairo --output ../compiled-contracts/account.json
popd

echo "compiling old..."

pushd starknet_0_9_1
poetry run cairo-compile ../contracts/simple-old.cairo --output ../compiled-contracts/simple-old.json
popd

echo "COMPILED"