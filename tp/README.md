# TP


## ngspice

Le dossier bin contient un exécutable pré-compilé qui peut être appelé 
pour lancer le simulateur :

```shell
cd bin/
./ngspice
```


Pour l'exécuter depuis n'importe où dans le terminal, lancer la commande 
suivante dans le dossier `bin` pour ajouter l'emplacement de ngspice à 
la variable d'environnement `PATH` :
```shell
export PATH=$(pwd):$PATH
```

> La variable PATH est une variable d'environnement, l'environnement est 
> lié à la session courante du terminal. Donc : nouveau terminal => 
> réinitialisation de PATH. On peut changer l'initialisation de 
> l'environnement, il y a un fichier qui est exécuté au lancement de 
> chaque nouveau terminal (~/.bashrc pour bash, ~/.zshrc pour zsh 
> (shell par défaut notamment sous Mac OS X)).


Si vous voulez builder vous-mêmes à la main ngspice, vous pouvez 
regarder le fichier build_ngspice.md. Cet exercice est recommandé.


## Python

Il est **fortement** recommendé d'utiliser un environnement virtuel 
python, un nouvel environnement peut être généré à l'aide de la 
commande suivante :
```shell
python3 -m venv env_name
```

Un dossier `env_name` est alors généré (choisissez un nom plus 
parlant). L'environnement peut être activé à l'aide de la commande :
```shell
source env_name/bin/activate
```

Le nom de l'environnement apparait alors devant le prompt entre 
parenthèses, montrant que l'environnement a été activé. Dès lors, dans 
le terminal courant, toutes les commandes python sont exécutées dans 
cet environnement, notamment lors de l'installation de package.

Les packages suivants sont requis ou complémentaires à la réalisation 
du TP :
```shell
python -m pip install --no-cache-dir stable-baselines3[extra] PySpice jupyterlab notebook seaborn packaging matplotlib pandas pytest tensorboard
```


### Sinon

L'ensemble de ces commandes peuvent être exécutées automatiquement en 
utilisant le script `activate_env.sh`, ce script **doit** être exécuté 
dans la session courante du terminal (c'est-à-dire à l'aide de la 
commande `source`) :
```shell
source activate_env.sh
```
Toutes les commandes précédentes sont alors exécutées dans un dossier 
temporaire du système qui sera effacé au redémarrage de l'ordinateur.


## Modèles

Le dossier `models` contient des modèles SPICE pour les transistors et 
sont à utiliser pour l'écriture des netlists. 
