#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

set -eu
set -x

datacube-ows-cfg check -i /env/config/inventory.json

set +x

