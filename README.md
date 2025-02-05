# Serpentin

Serpentin est un logiciel Saas permettant de calculer les primes de commerciaux de facon très simple. Le principe est le
suivant :

* Des sales (commerciaux) vont gagner des deals et sont rémunérés en fonction. Seuls les deals closed sont utilisés pour le commissionnement.
* On peut créer des commissions de différent types
* Pour chaque sales, on calcule une fiche de paye pour tous les mois (un statement)

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


## Votre mission

* Implémenter la compensation simple et faire les managers + api + ui en suivant l'exemple des deals.
* Implémenter la création de statement et faire les managers + api + ui.
* Ajouter un flag `draft` sur les compensations pour qu'elles ne soient pas comptées.
* Implémenter la compensation complexe.
