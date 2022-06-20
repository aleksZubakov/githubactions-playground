#!/usr/bin/env nix-shell
#! nix-shell build.nix -A shell -i bash

python -m unittest # discover -s ./tests | tee ./test_output
python -m wheel
exit 0
