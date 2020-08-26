#!/usr/bin/env sh

set -euo pipefail

echo 'number 1' || test && echo 'sneak me in!' || echo 'nope it broke' 
