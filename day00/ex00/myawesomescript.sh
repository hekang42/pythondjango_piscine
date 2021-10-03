#!/bin/sh
curl -sI {$1} | grep Location | cut -c 11-