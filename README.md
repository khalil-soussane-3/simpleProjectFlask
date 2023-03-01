# simpleProjectFlask
gestion des reseaux neurounes avec flask
Presentation de projet :
  On cherche à concevoir et développer une application pour pouvoir classifier des données en
utilisant un algorithme d’apprentissage. Pour ce, on va créer des réseaux de neurones
artificiels pour simuler le fonctionnement du cerveau humain. Il s'agit d'outils permettant de
classifier, de détecter des régularités, d’optimiser etc. On trouve plusieurs types de réseaux de
neurones, qui possèdent tous un composant de base : le neurone.
  Un neurone est une unité de traitement qui prend des entrées et renvoie un résultat moyennant
une fonction particulière. On peut supposer que le type des valeurs manipulées en entrée et en
sortie par les neurones dépend du type de réseau que l’on utilise.
Un réseau de neurones est organisé en couches reliées entre elles. On y trouvera deux couches
particulières, la couche d’entrée contenant les neurones qui reçoivent les valeurs d’entrées du
réseau et la couche de sortie contenant les neurones qui renvoient les valeurs de sortie du
réseau. Un neurone d’une couche i peut être relié à un ou plusieurs neurones d'une couche
i+1. Un poids est associé à chaque connexion entre neurones. Comme un neurone peut avoir
les sorties de plusieurs neurones en entrées, une fonction de combinaison permet d’agréger les
différentes entrées en utilisant les poids associés. Il en existe de plusieurs types : fonction
utilisant la valeur maximale, la valeur minimale, le produit, la somme, une moyenne, un «ou »
logique des entrées. De la même façon, la valeur de sortie d’un neurone peut être calculée en
utilisant différentes fonctions de transfert : Heaviside, linéaire, sigmoïde, etc.
  Il est possible aussi d’associer à un réseau une fonction d’apprentissage, qui va permettre de
corriger les valeurs des poids des connexions. Pour cela, on dispose d’un ensemble de
mesures cibles et on peut connaître l’erreur entre la sortie de chaque neurone et le résultat
attendu. Différentes fonctions d’apprentissage sont disponibles : fonctions d’apprentissage
itératives, parmi lesquelles on trouve des fonctions d’apprentissage supervisées (propagation
arrière par exemple) ou non supervisées, comme la fonction d’apprentissage de Hopfield, la
fonction d’apprentissage de Kohonen etc.
  Enfin, voici les grands types de réseaux :
   le plus simple est le perceptron, qui utilise des valeurs binaires et possède deux
couches;
   le perceptron multi-couches est une évolution du perceptron qui accepte plusieurs
couches «cachées » entre la couche d’entrée et la couche de sortie. Il utilise un
apprentissage par propagation arrière;
   le réseau de Hopfield, qui ne possède pas de couche cachée, qui utilise la fonction
d’apprentissage de même nom et dans lequel tous les neurones sont connectés entre
eux ;
   le réseau de Kohonen, qui utilise la fonction d'apprentissage du même nom et des
valeurs réelles.
  Le cycle de vie d’un réseau de neurone est caractérisé par deux grands cas : soit il est en mode
d’apprentissage, soit il est en mode «normal ». En mode d’apprentissage, le réseau attend un
exemple, calcule la sortie correspondant à l’entrée de
l’exemple, compare cette sortie à la sortie de l’exemple et ajuste les poids en conséquence.
En mode «normal », le réseau attend une entrée, calcule la sortie et la fournit.
On passe d’un mode à l’autre grâce à un signal particulier.
