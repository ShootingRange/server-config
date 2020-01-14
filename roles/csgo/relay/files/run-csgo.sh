#!/bin/sh

export LD_LIBRARY_PATH=/home/steam/csgo/bin:/home/steam/csgo:/home/steam/csgo/bin
exec /home/steam/csgo/srcds_linux \
  -game csgo \
  -net_port_try 1 \
  -tickrate 128 \
  -ip 0.0.0.0 \
  -port $SERVER_PORT \
  -usercon \
  -lan 0 \
  +sv_lan 0 \
  +sv_setsteamaccount "${GSLT}" \
  +tv_port "${GOTV_PORT}" \
  +tv_relaypassword "${GOTV_RELAY_PASSWORD}" \
  +rcon_password "${RCON_PASSWORD}" \
  +password "${GOTV_PASSWORD}" \
  +exec "instance_${1}.cfg" \


#  +sv_password "$PASSWORD" \
