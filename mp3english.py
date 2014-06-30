#-------------------------------------------------------------------------------
# Name:        Mp3 Searcher
# Purpose:     Search any song and download it
#
# Author:      overloadfull
# Collaborator:kenkeiras
# Created:     30/06/2014
# Copyright:   (c) overloadfull 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib2,urllib
import os

def main(a1):
    busq = raw_input("Search song(title first and singer next if possible)      >> ")
    busq.replace(" ", "_")
    openn = urllib2.urlopen("http://www.mp3skull.com/mp3/"+busq+".html")
    reaad = openn.read()
    for i in str(reaad):

        a1 = reaad.find('<div style="float:left;"><a href="',a1+10)
        a2 = reaad.find('http://',a1)#5134
        a3 = reaad.find('.mp3" ',a2)#5215
        a4 = reaad[a2:a3+4].replace(" ","_")
        print a4
        if i > len(reaad):
              break
    descargar(a4,reaad,a1,busq)
    openn.close()
def descargar(url,reaad,a1,busq):

    try:
     busq2 = urllib2.Request(url)
     baj = urllib2.urlopen(busq2)
     datos = baj.read()
     mp3nombre = busq+".mp3"
     cancion = open(mp3nombre, "wb")
     cancion.write(datos)
     cancion.close()
     print "Your song is in: "+ os.getcwd() #directorio (a?adir que se pueda cambiar el directorio)
     print "Check your song's version before answering if you want another      version."
     opt = raw_input("Do you want another version of the song?(s/n)>> ")
     if opt == "s":
          main(a1)
     elif opt =="n":
          opt2 = raw_input("Exit?(s/n)>> ")
          if opt2 == "s":
            exit()
          elif opt2 == "n":
            main()
          else:
            print "Type a valid option"
            main()
     else:
         print "Type a valid option"
         exit
    except urllib2.HTTPError: #si no se encuentra..
        print Exception("Link no encontrado")

        opt = raw_input("Quiere otra version?(s/n)>> ")
        if opt == "s":
          main(a1)
        elif opt =="n":
          opt2 = raw_input("Quiere salir?(s/n)>> ")
          if opt2 == "s":
            exit()
          elif opt2 == "n":
            main()
          else:
            print "Introduzca una opcion valida"
            main()
        else:
         print "Introduzca una option valida"
        exit
main(1)

