#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys, os, json, requests

reponse = requests.get("http://localhost:5000/recherche/"+sys.argv[1])
reponses = reponse.json()

for reponse in reponses :
    print(reponse[0])
    print(reponse[1])
    print("--------------------")
