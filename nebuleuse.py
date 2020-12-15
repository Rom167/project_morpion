#january3
#pour faire des jeu :
#turtle
#Pygame
#Tkinter


                    # version française (ajout des niveaux de difficluté : ils changent la valeur de max_delay)


#import winsound
import time

 
print('\n' + "Les deux joueurs sont:")
joueur1 = input("joueur1 : ")
joueur2 = input("joueur2 : ")
 
assert joueur1 != joueur2, "Tu ne peux pas jouer contre toi même..."
 
with open("scores_test3.txt", "a") as f:
    f.write('') 
with open("scores_test3.txt", "r") as f:
    contenu_total = f.readlines()


if str(joueur1) + ' :' + '\n' in contenu_total and str(joueur2) + ' :' + '\n' in contenu_total :
    assert contenu_total.index(str(joueur1) + ' :' + '\n') < contenu_total.index(str(joueur2) + ' :' + '\n'), "Joueur 1 et joueur 2 sont inversés..."


print('\n')

p=dict([(1,'○'),(2,'☺'),(3,'Ø'),(4,'♂'),(5,'♀'),(6,'§'),(7,'▲'),(8,'®'),(9,'□')])
d=dict([(1,'\u25CB'),(2,'\u263A'),(3,'\u00D8'),(4,'\u2642'),(5,'\u2640'),(6,"\u00A7"),(7,'\u25B2'),(8,'\u00AE'),(9,'\u25A1')])
for k in p.items() :
    print(k)
 
L_dico = [k for k in d.items()]
 
print('\n' + "Quel symbole choisis-tu ? (tu peux choisir dans le dictionnaire ci-dessus)" + '\n')
 
symbole1 = input("symbole " + joueur1 + " : ")
symbole2 = input("symbole " + joueur2 + " : ")
 
assert symbole1 != '', "Il faut choisir un symbole !"
assert symbole2 != '', "Il faut choisir un symbole !"
assert symbole1 != symbole2, "Il ne faut pas choisir le même symbole"
 
 
for y in range (1,10):
    if symbole1 == str(y):
        symbole1 = d.get(y)
        print('\n' + 'nouveau symbole de ' + joueur1 + ' : ' + symbole1)
    
for z in range (1,10):
    if symbole2 == str(z):
        symbole2 = d.get(z)
        print('nouveau symbole de ' + joueur2 + ' : ' + symbole2 + '\n')
 
 
#print("Quel niveau de difficulté ?")
#input("niveau de dfficulté (1, 2 ou 3) : ") + fonctions associées à 1, 2 ou 3
 

dico_joueurs = dict([(joueur1,symbole1), (joueur2,symbole2)])

for q in dico_joueurs.items() :
    print(q)



print('\n' + "Quelle taille pour la grille ?")
n = int(input("n = "))


print('\n' + "Quel niveau de difficulté ? ")
print("     --> 1 : facile, 60s pour faire ton coup")
print("     --> 2 : moyen, 30s")
print("     --> 3 : difficile, 10s")
print("     --> personnalisé : le nombre que tu inscris sera le nombre de secondes que tu auras" + '\n')
time_input = int(input("Temps par coup (en secondes) = "))

print('\n')

grille=[]
 
for i in range(n):
    grille.append([])
    
    for j in range(n):
        grille[i].append(' ')
    
 
for k in range(n):
    print(grille[k])
   
 
 
def alignements_colonne(grille, colonne, ligne):
  
    c = 0
    
    for i in range(0, n):
        if grille[ligne-1][colonne-1] != ' ':
            if grille[ligne-1][colonne-1] == grille[i][colonne-1] :
                c += 1
    if c == n : return True
    else :
        return False
 
 
def alignements_ligne(grille, colonne, ligne):
  
    l = 0
    
    for i in range(0, n):
        if grille[ligne-1][colonne-1] != ' ':
            if grille[ligne-1][colonne-1] == grille[ligne-1][i] :
                l += 1
    if l == n : return True
    else :
        return False
 
 
def alignements_diag1(grille, colonne, ligne):
  
    d1 = 0
    
    for i in range(0, n):
        if grille[ligne-1][colonne-1] != ' ':
            if grille[ligne-1][colonne-1] == grille[i][i] :
                d1 += 1
    if d1 == n : return True
    else :
        return False
 
 
def alignements_diag2(grille, colonne, ligne):
  
    d2 = 0
    
    for i in range(0, n):
        if grille[ligne-1][colonne-1] != ' ':
            if grille[ligne-1][colonne-1] == grille[(n-1)-i][i] :
                d2 += 1
    if d2 == n : return True
    else :
        return False
 
 
 
def joue(grille, joueur, autre_joueur, time_input): 

    add_time = 0
    now = time.time()
    assert ligne-1 > n and colonne-1 > n, print("vous avez saisi un nombre trop grand, c'est à l'autre joueur de jouer")

    if time_input == 1 :
        add_time += 60
    elif time_input == 2 :
        add_time += 30
    elif time_input == 3 :
        add_time += 10
    else :
        add_time += time_input
        
    max_delay = now + add_time

    print('\n' + '\n' + "C'est à " + joueur + " de jouer...") #on mettra une fct aléatoire
    colonne = int(input('\n' + "Entrez le numéro de la colonne : "))

    if time.time() <= max_delay :

        ligne   = int(input("Entrez le numéro de la ligne : "))    

        if time.time() <= max_delay :       
            if grille[ligne-1][colonne-1] == ' ':
                grille[ligne-1][colonne-1] = dico_joueurs.get(joueur)
                print ('\n' + joueur + " a joué la case (" + str(colonne) + "," + str(ligne) + ")" + '\n')

            else :
                print ('\n' + 'Erreur : case déjà jouée. Tu triches ! ' + autre_joueur + ' reprend la main.' + '\n')

        else :
            print('\n' + 'Erreur : ' + str(joueur) + ' : tu as mis trop de temps à jouer ! Coup invalidé. ' + autre_joueur + ' reprend la main.' + '\n')

    else :
        print('\n' + 'Erreur : ' + str(joueur) + ' : tu as mis trop de temps à jouer ! Coup invalidé. ' + autre_joueur + ' reprend la main.' + '\n')

        
    for l in range(n):
        print(grille[l])
 


 
def game():
 
    no_win = True
    no_win2 = True
    
    L1 = []
    L2 = []
    L3 = []
    L4 = [0,0]

    t = 1
    
    while no_win :
    
        if t <= n*n :
    
            joue(grille, joueur1, joueur2, time_input)
                    
            t += 1
    
            for k in range(0,n):
                for l in range (0,n):
                    if alignements_colonne(grille, k, l)  :
                        L1.append('win')
                        L3.append(joueur1)
                    elif alignements_ligne(grille, k, l)  :
                        L1.append('win')
                        L3.append(joueur1)
                    elif alignements_diag1(grille, k, l)  :
                        L1.append('win')
                        L3.append(joueur1)
                    elif alignements_diag2(grille, k, l)  :
                        L1.append('win')
                        L3.append(joueur1)
    
            if 'win' in L1 :
                L4[0] = 1
                no_win = False
                no_win2 = False
            else :
                no_win = False
                no_win2 = True
        else :
            return '\n' + 'Fin de la partie. Match nul.'
                
        while no_win2 :
    
            if t <= n*n :    
    
                joue(grille, joueur2, joueur1, time_input)
    
                t += 1
    
                for k in range(0,n):
                    for l in range (0,n):                   
                        if alignements_colonne(grille, k, l):
                            L2.append('win')
                            L3.append(joueur2)
                        elif alignements_ligne(grille, k, l):
                            L2.append('win')
                            L3.append(joueur2)
                        elif alignements_diag1(grille, k, l):
                            L2.append('win')
                            L3.append(joueur2)
                        elif alignements_diag2(grille, k, l):
                            L2.append('win')
                            L3.append(joueur2)
    
                if 'win' in L2 :
                    L4[1] = 1
                    no_win2 = False
                    no_win = False
                else :
                    no_win2 = False
                    no_win = True     
    
            else :
                return '\n' + 'Fin de la partie. Match nul.' 

    



    with open("nb_game.txt", "a") as f:
        f.write('\n' + '0')  

    with open("nb_game.txt", "r") as f:
        elements = f.readlines()

        if len(elements) == 2:
            dernier_element = int(elements[-1])
        else :
            dernier_element = int(elements[-2])
        
        dernier_element += 1

    with open("nb_game.txt", "a") as f:
        f.write(str(dernier_element))  

    


    with open("scores_test3.txt", "a") as f:
        f.write('\n' + '\n' + 'Match entre ' + str(joueur1) + ' et ' + str(joueur2) + ' :') 


    if dernier_element == 1 :

        print ('\n' + "Partie numéro 1 :" + '\n')
        with open("scores_test3.txt", "a") as f:
            f.write('\n' + joueur1 + ' :' + '\n' + str(L4[0]) + '\n' + joueur2 + ' :' + '\n' + str(L4[1]))   

        winsound.Beep(440, 500)
        print ('win ! ' + 'Fin du jeu : ' + 'victoire de ' + L3[0] + '\n')
        return 'Score de ' + str(joueur1) + ' : ' + str(L4[0]) + '\n' + 'Score de ' + str(joueur2) + ' : ' + str(L4[1])        

    else :
        print ('\n' + "Partie numéro " + str(dernier_element) + " :" + '\n')

        with open("scores_test3.txt", "r") as f:
            l = f.readlines()

        
        if str(joueur1) + ' :' + '\n' in l and str(joueur2) + ' :' + '\n' in l :

            liste_ensemble = list(enumerate(l,1)) 
            L_match = []


            for i in range(len(liste_ensemble)):
                if liste_ensemble[i][1] == 'Match entre ' + str(joueur1) + ' et ' + str(joueur2) + ' :' + '\n' :
                    L_match += [liste_ensemble[i][0]]


            def maximum(liste):
                maxi = liste[0]
                for u in liste:
                    if u >= maxi:
                        maxi = u
                return maxi


            a = int(l[(maximum(L_match))+1])
            b = int(l[(maximum(L_match))+3])


            if L4[0] == 1 :
                a += 1
            elif L4[1] == 1 :
                b += 1

            L4[0] = a
            L4[1] = b

            with open("scores_test3.txt", "a") as f:
                f.write('\n' + joueur1 + ' :' + '\n' + str(L4[0]) + '\n' + joueur2 + ' :' + '\n' +  str(L4[1])) 

        else :
            with open("scores_test3.txt", "a") as f:
                f.write('\n' + joueur1 + ' :' + '\n' + str(L4[0]) + '\n' + joueur2 + ' :' + '\n' +  str(L4[1]))  

        winsound.Beep(440, 500)
        print ('win ! ' + 'Fin du jeu : ' + 'victoire de ' + L3[0] + '\n')
        return 'Score de ' + str(joueur1) + ' : ' + str(L4[0]) + '\n' + 'Score de ' + str(joueur2) + ' : ' +  str(L4[1])

 
  
  

            #function to run it all

print(game())