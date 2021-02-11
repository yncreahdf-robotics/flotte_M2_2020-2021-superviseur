#!/bin/bash
sudo service mysql stop
sudo service mosquitto stop
sudo docker-compose up -d && sudo docker-compose exec superviseur python Main.py sh
