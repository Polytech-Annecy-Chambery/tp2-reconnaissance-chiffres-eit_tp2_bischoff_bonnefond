from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    
    i = image.binarisation(S)
    imag = i.localisation()
    liste_simi=[]
    
    for mod in liste_modeles:
        
        imag_redim = imag.resize(mod.H, mod.W)
        simi = imag_redim.similitude(mod)
        liste_simi.append(simi)
        
        
    return (liste_simi.index(max(liste_simi)))
    
