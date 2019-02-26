#!/bin/sh

export LD_LIBRARY_PATH=/home/steam/csgo/bin:/home/steam/csgo:/home/steam/csgo/bin
exec /home/steam/csgo/srcds_linux \
  -game csgo \
  -net_port_try 1 \
  -tickrate 128 \
  -ip 0.0.0.0 \
  -port $SERVER_PORT \
  -usercon \
  +sv_setsteamaccount "$GSLT" \
  +tv_port "$GOTV_PORT" \
  +tv_password "$GOTV_PASSWORD" \
  +tv_relaypassword "${GOTV_PASSWORD}_ggwrelay" \
  +sv_password "$PASSWORD" \
  +rcon_password "$RCON_PASSWORD" \
  +mapgroup mg_active \
  +map de_dust2 \
  +exec "instance_${1}.cfg" \
