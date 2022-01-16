# Serpentin

Serpentin est un logiciel Saas permettant de calculer les primes de commerciaux de facon très simple. Le principe est le
suivant :

* Des sales (commerciaux) vont gagner des deals et sont rémunérés en fonction. Seuls les deals closed sont utilisés pour le commissionnement.
* On peut créer des commissions de différent types
* Pour chaque sales, on calcule une fiche de paye pour tous les mois (un statement)

Le but de cet exercice est d'implémenter les calculs de compensations ainsi que l'API associée, puis de mettre en oeuvre
ses talents de webdesigner en créant l'interface de présentation de ces statements.

## Setup

### API

L'API est faite en Python avec le framework Flask, il faut donc créer de préférence un virtualenv et installer les
dépendances nécessaires.

```
$ cd api/
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Le provisionning de la base de donnée est lui aussi fait en Python et doit être lancé :

```
(venv) $ python provision.py
```

Afin de lancer le backend, il reste alors :

```
(venv) $ python run.py
```

### UI

L'UI est elle développée en VueJS et se lance classiquement avec :

```
$ cd ui/
$ npm install
$ npm run dev
```

Le framework UI utilisé est Vuetify et devra être utilisé pour les écrans. Le framework front est NuxtJS.

## Compensations

### Simple

Une compensation de type Simple est définie par :

* On fait la somme des montants closed dans le mois par un commercial
* Si le nombre de deals closed est supérieur à 4
    * On prend 20% de cette somme
* Sinon
    * On prend 10% de cette somme
* Si le montant est inférieur à 500€, il est plafonné par le bas à 500€

### Complexe

Pour cette compensation, il est necessaire d'ajouter une `target` sur les commerciaux. Une compensation de type Complexe
est alors définie par :

* On fait la somme des montants closed dans le mois par un commercial
* On calcul le *Target achievement* du commercial : Somme / Target
* On applique sur ce Target achievement un accélérateur dont le fonctionnement est similaire aux tranches d'impositions.
  On applique le taux uniquement à la somme contenue entre les tranches.
    * Si le nombre est entre 0% et 50%, la tranche vaut 0
    * Si le nombre est entre 50% et 100%, la tranche vaut 8% de la Somme
    * Si le nombre est entre 100% et 150%, la tranche vaut 12% de la Somme
    * Au dela, la tranche vaut 16% de la Somme
* Un bonus de 500€ est attribué si le nombre de deal (meme non-closés) dans le mois est supérieur à 7.

## Votre mission

* Implémenter la compensation simple et faire les managers + api + ui en suivant l'exemple des deals.
* Implémenter la création de statement et faire les managers + api + ui.
* Ajouter un flag `draft` sur les compensations pour qu'elles ne soient pas comptées.
* Implémenter la compensation complexe.
