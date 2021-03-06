# Saph_211_Ethernet
Projet de ENS-PS, Saphire 211

## Modélisation du domaine de collision:
Le domaine est composé de plusieurs machines. On represente tout cela sous la forme de machines à états. Chaque machines du dommaines est une machines à états differente, et le dommaine en est une autre.

### Les machines:

![Diagramme d'état d'une machine](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.github.com/EmileClement/Saph_211_Ethernet/master/asset/etat_machine.uml&fmt=svg)

Les états sont:
* `Idle` : La machine ne fait rien, elle attend de devoir envoyer un message.
* `Initial` : La machine commence à emmetre, elle occupe le dommaine sans pour autant que les autres puissent la detecté.
* `Transmition` : La machine transmet sont message depuis sufisament longtemps pour que toutes les machines aient détécté que le domaine etait occupé.
* `Attente_O` : La machine attend que le domaine sois libre pour parler.
* `Fin_initial` : La machine a détécté une collision mais s'assure que toute les autres machines aient détécté la collison.
* `Attente_C` : La machine attent un temps aléatoire avant de parler.

### Le domaine:

![Diagramme d'état du domaine](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.github.com/EmileClement/Saph_211_Ethernet/master/asset/etat_domaine.uml&fmt=svg)

Les états sont:
* `Libre` : Aucune machine ne parle.
* `Risque` : Une seule machine parle et il n'y a pas encore eu de collision.
* `Occupe` : Une seule machine parle depuis sufisament longtemps pour que il n'y ais plus de collison.
* `Collision` : Une collision a eu lieu, on attend que toutes les machines se taisent.

### Les transition:

|     Etat \ Event     	| `Event_Fin_transmition` 	| `Event_Fin_initial` 	| `Event_Fin_alea` 	| `Event_Debut_parlant` 	| `Event_Volonte_msg` 	|   	|   	|
|:--------------------:	|:-----------------------:	|:-------------------:	|:----------------:	|:---------------------:	|:-------------------:	|:-:	|:-:	|
|    `Etat_D_Libre`    	|                         	|                     	|                  	|                       	|                     	|   	|   	|
|    `Etat_D_Risque`   	|                         	|                     	|                  	|                       	|                     	|   	|   	|
|    `Etat_D_Occupe`   	|                         	|                     	|                  	|                       	|                     	|   	|   	|
|  `Etat_D_Collision`  	|                         	|                     	|                  	|                       	|                     	|   	|   	|
|     `Etat_M_Idle`    	|                         	|                     	|                  	|                       	|                     	|   	|   	|
|     `Etat_M_Idle`    	|                         	|                     	|                  	|                       	|                     	|   	|   	|
| `Etat_M_Attente_O`   	|                         	|                     	|                  	|                       	|                     	|   	|   	|
| `Etat_M_Initial`     	|                         	|                     	|                  	|                       	|                     	|   	|   	|
| `Etat_M_Transmition` 	|                         	|                     	|                  	|                       	|                     	|   	|   	|
| `Etat_M_Fin_initial` 	|                         	|                     	|                  	|                       	|                     	|   	|   	|
| `Etat_M_Attente_C`   	|                         	|                     	|                  	|                       	|                     	|   	|   	|

## Modélisation informatique:

![Diagramme des Classes](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.github.com/EmileClement/Saph_211_Ethernet/master/asset/class.uml&fmt=svg)

### test 4

## Modelisation des cables
https://fr.wikipedia.org/wiki/%C3%89quations_des_t%C3%A9l%C3%A9graphistes

## Outils:
planttext.com
