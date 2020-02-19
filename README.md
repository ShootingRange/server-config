# GGW server configuration

This repository contains an [Ansible](https://www.ansible.com/) playbook for that setup and configure Counter Strike: Global Offensive servers and other related services used during the Geeks Gone Wild LANs.

The playbook have been tested on Ubuntu 18.04 with Ansible 2.9.4.

Clone the repository using the following command to get all files:
```
git clone --recurse-submodules https://github.com/LanTeamNord/server-config.git
```

## Services

The following service will be configure by the playbook

 - [Counter-Strike: Global Offensive](https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/) dedicated server
 - [Get5](https://github.com/splewis/get5): CS:GO Sourcemod plugin for competitive matches/scrims
 - [Get5-web](https://github.com/PhlexPlexico/get5-web/): Webpanel for servers using the get5 CS:GO server plugin
 - Automatic demo uploader for uploading CS:GO demoes to a remote server
 - Firewalld
 - MySQL server for get5-web and get5-mysqlstats
 - [eBot](https://github.com/deStrO/eBot-CSGO), CS:GO server manager [deprecated]
