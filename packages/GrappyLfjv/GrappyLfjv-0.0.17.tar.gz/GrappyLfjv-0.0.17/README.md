# Grappy

Grappy est une librairie Python basée sur matplotlib, qui simplifie la création de graphiques.

## Installation

Vous pouvez Installer Grappy avec [pip](https://pypi.org/project/GrappyLfjv/)

```bash
pip install GrappyLfjv
```

## Guide d'utilisation

Création graphique à partir de points:

```python
from grappy import graphe

exemple = graphe("Nom graphique", "labelx", "labely").points([(3,4),(6,5),(8,9)]).afficher()
```

Exportation graphique vers fichier csv:

```python
from grappy import graphe

exemple = graphe("Nom graphique", "labelx", "labely").points([(3,4),(6,5),(8,9)]).exporter("nomFichier")
```

Importation depuis csv:

```python
from grappy import graphe

exemple = graphe().importer("nomFichier", "h").afficher()

#h si tableau horizontale, v si verticale
```

Créatin graphique à partir d'une fonction:

```python
from grappy import graphe

exemple = graphe().fonction("x**2+2", 0, 100)
```

Merci de vous référer à la documentation pour plus plus d'informations

## Documentation

## License

[MIT](https://choosealicense.com/licenses/mit/)
