#imports
from random import randint
#Equipe Class
class Equipe():
    def __init__(self,Nom,NB_Match,Total_Point,NB_Victoire,NB_Defait,NB_Match_Null,But_Marque,But_Concede):
        self.Nom=Nom
        self.NB_Match=NB_Match
        self.Total_Point=Total_Point
        self.NB_Victoire=NB_Victoire
        self.NB_Defait=NB_Defait
        self.NB_Match_Null=NB_Match_Null
        self.But_Marque=But_Marque
        self.But_Concede=But_Concede
    #affichage Function
    def Affichage(self):
        print(self.__dict__)

 #calcul point Function
    def Calcul_Point(self):
          self.Total_Point +=(self.NB_Victoire*3)+self.NB_Match_Null+(self.NB_Defait*0)
          return self.Total_Point


    #goal average(moyenne) Function
    def Goal_Average(self):
        return self.But_Marque-self.But_Concede
#Poule Class
class Poule():
    def __init__(self,Poule_Name):
        self.Poule_Name=Poule_Name
        self.Equipes=list()

 #affichage Function
    def Afficher(self):        
        print('NOM de POULE :%s' % self.Poule_Name) 
        [Equipe.Affichage() for Equipe in self.Equipes]

 #ajout equipe Function
    def Ajouter_Equipe(self,obj):
        if (len(self.Equipes)>3):
            print("__ limite exited __")
            pass
        else:
            self.Equipes.append(obj)#mapper
     #supprimer Function
    def Supprimer_Equipe(self,nom):
        for _,Equipe in enumerate(self.Equipes):
            if Equipe.__dict__['Nom']==nom:
                del self.Equipes[_]

  #Somme des butes Function
    def Total_Buts_Marque(self):
        return sum([_.__dict__['But_Marque'] for _ in self.Equipes])

#qualifier une equipe Function
    def Qualification(self):
 
            [print(e.Calcul_Point()) for e in self.Equipes]
            tirage=[e.Total_Point for e in self.Equipes]
            avg=[e.Goal_Average() for e in self.Equipes]
            E1=(max(tirage))
            E1_pos=tirage.index(max(tirage))
            tirage.remove(max(tirage))
            E2=max(tirage)
            E2_pos=tirage.index(max(tirage))+1
            if (E1!=E2):
                return self.Equipes[E1_pos].Nom,self.Equipes[E2_pos].Nom
            elif(E1==E2):
                E1=(max(avg))
                E1_pos=avg.index(max(avg))
                avg.remove(max(avg))
                E2=max(avg)
                E2_pos=avg.index(max(avg))+1
                return self.Equipes[E1_pos].Nom,self.Equipes[E2_pos].Nom
            else:
                return self.Equipes[randint(0,3)].Nom,self.Equipes[randint(0,3)].Nom

#Main Program
if __name__ == "__main__":

    poule=Poule('A')
    E1=Equipe('EST',5,0,3,1,2,4,6)
    E2=Equipe('ESS',5,0,5,0,0,15,2)
    E3=Equipe('CSS',5,0,2,2,1,2,6)
    E4=Equipe('CAB',5,0,1,2,2,2,1)
    poule.Ajouter_Equipe(E1)
    poule.Ajouter_Equipe(E2)
    poule.Ajouter_Equipe(E3)
    poule.Ajouter_Equipe(E4)
    
    for e in poule.Equipes:
        e.Affichage()
        print('Total Point : %s ' % e.Total_Point)
        print('Average Goals: %s' % e.Goal_Average())
    e1,e2=poule.Qualification()
    print("Equipe Qualife E1={} ,E2={}".format(e1,e2))
    for e in poule.Equipes:
        e.Affichage()