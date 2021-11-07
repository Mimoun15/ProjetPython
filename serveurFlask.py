#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, json, re
os.system("clear")

from flask import Flask
app = Flask(__name__)

@app.route('/')  # route localhost:5000
def index():
   return "Ceci est la page d'accueil."

@app.route('/hello/<phrase>')
def hello(phrase):
   return "Bonjour "+phrase

@app.route('/references')
def references():
   print("/references")
   references = []
   liste = os.listdir("PAGES")
   for fichier in liste :
      print(fichier)
      fd = open("PAGES/"+fichier)
      for ligne in fd.readlines() :
         resultat = re.search("\[\[(.+?)\]\]", ligne)  # L'expression régulière est à trouver
         if resultat :
            references.append(resultat.group(1))
   return json.dumps(references)

@app.route('/recherche/<critere>')
def recherche_critere(critere):
   print("/recherche/"+critere)
   lignes = []
   liste = os.listdir("PAGES")
   for fichier in liste :
      print(fichier)
      fd = open("PAGES/"+fichier)
      for ligne in fd.readlines() :
         res1 = re.search("\[\[(.+?)\]\]", ligne)  # L'expression régulière est à trouver
         res2 = re.search(""+critere, ligne)         
         if res1 and res2 :
            lignes.append(ligne)
   return json.dumps(lignes)

app.run()
