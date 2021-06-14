#!/bin/sh
curl -sI {$1}  | grep ocation | cut -c 11-