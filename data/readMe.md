### SecondHandCar
La société SecondHandCar vend, achète et répare des voitures. Sa surface de vente peut accueillir 100 voitures et son garage 50.
Les voitures en vente peuvent bénéficier d'un bonus écologique. Chaque jour, la comptabilité doit obtenir le reporting des ventes
de voitures, des réparations, des achats de voiture et de pièces détachées.

Inclure une propriété dépendante Modèle Complet qui restitue la marque, le modèle et l'énergie.
Exemple : Ford Escort RS Turbo Essence

### Exercice 
Créer les classes permettant de representer le SI de SecondHandCar

### Structure perso
Voiture ( Id, Marque, Modele, Énergie )
Surface_vente ( Voitures , Capacité )
Garage ( Voitures, Capacité, Réparations )
Réparation ( Id, date, prix, Voiture )
Achat ( Id, date, prix, Voiture )  
Vente ( Id, date, prix, Voiture )