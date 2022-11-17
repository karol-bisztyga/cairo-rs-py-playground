#!/bin/bash

set -e

# make sure you're not in the poetry shell or this script may not work

echo "initializing new starknet..."

pushd starknet_0_10_1
CFLAGS=-I`brew --prefix gmp`/include LDFLAGS=-L`brew --prefix gmp`/lib poetry run pip install ecdsa fastecdsa sympy
poetry run pip install cairo-lang
popd

echo "initializing old starknet..."

pushd starknet_0_9_1
CFLAGS=-I`brew --prefix gmp`/include LDFLAGS=-L`brew --prefix gmp`/lib poetry run pip install ecdsa fastecdsa sympy
poetry run pip install -Iv cairo-lang==v0.9.1
popd

echo "INITIALIZED"