#!/bin/bash
rm -rf ../templates
mkdir -p ../templates
ng build --outputPath=../templates --prod  --outputHashing=all

