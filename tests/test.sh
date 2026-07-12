#!/bin/bash

mkdir -p /logs/verifier
pytest /tests/test_outputs.py -rA --ctrf=/logs/verifier/ctrf.json
status=$?
echo $((status == 0)) > /logs/verifier/reward.txt

exit "$status"
