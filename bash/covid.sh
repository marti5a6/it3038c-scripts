#!/bin/bash

# This script dowbnloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
DEATHS=$(echo $DATA | jq '.[0].death')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative COVID cases, $HOSPITALIZED hospitalized, and $DEATHS deaths."
