#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, json, re
os.system("clear")

from flask import Flask, render_template
app = Flask(__name__)
app._static_folder = os.path.abspath("./")
picFolder = os.path.join('lavande.jpg')



@app.route("/")
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg')
    return render_template("recherche_1.html", user_image=pic1)

   
@app.route('/recherche')  # route qui renvoie la page HTML recherche.html
def recherche():
   print('/recherche')
   if os.path.isfile("recherche.html") :
       return app.send_static_file("recherche.html")
   return "recherche.html non accessible"
   
@app.route('/recherche_1')  # route qui renvoie la page HTML recherche_1.html
def recherche_1():
   print('/recherche_1')
   if os.path.isfile("recherche_1.html") :
       return app.send_static_file("recherche_1.html")
   return "recherche_1.html non accessible"

@app.route('/recherche/<critere>')
def recherche_critere(critere):
  x=critere.split()
  print("/recherche/"+critere)
  lignes = []
  liste = os.listdir("PAGES")
  for fichier in liste :
      fd = open("PAGES/"+fichier)
      for ligne in fd.readlines() :
       i=0
       for a in x :
           res2 = re.search(""+a, ligne)         
           if res2:
            i=i+1
       if i==len(x):     
             lignes.append([fichier,ligne])  # Le nom de la page est envoyée avant la ligne dans une sous-liste
  return json.dumps(lignes)

app.run()
