#!/bin/bash

NAME="$(hostname)"

find /home/steam/csgo/csgo -maxdepth 1 -name "*.dem" | xargs -n 1 -I {} /home/steam/rclone sync {} ltn-hltv:${NAME}/
