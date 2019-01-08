#!/bin/sh

/home/steam/csgo/srcds_linux \
  -net_port_try 1 \
  +sv_setsteamaccount $GSLT \
  rcon_password $RCON_PASSWORD
