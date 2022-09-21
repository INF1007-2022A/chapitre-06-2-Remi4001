#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # Transformer la liste en dictionnaire,
    # les éléments de la liste deviennent les clés
    # et leur index deviennent les valeurs
    dictionnaire = {}
    
    for i in range(len(some_list)):
        dictionnaire[some_list[i]] = i

    return dictionnaire


def color_name_to_hex(colors: list) -> list:
    # Trouver la valeur hex de chaque couleur dans la liste
    # et créer une liste de tupple où le premier élément est
    # le nom de la couleur et le deuxième est la valeur hex
    hex_list = []

    for color in colors:
        hex_list.append((color, cnames[color]))

    return hex_list


def create_list() -> list:
    # Créer une liste des 10 000 premiers entiers positif,
    # sauf pour les entiers de 15 à 350
    liste = []

    for i in range(15):
        liste.append(i)

    for i in range(351, 10000):
        liste.append(i)

    return liste


def compute_mse(model_dict: dict) -> dict:
    # Calculer l'erreur quadratique moyen pour chaque modèle.
    # Retourner un dictionnaire contenant les MSE.
    resultats = {}

    for name, values in model_dict.items():
        somme = 0

        for entry in values:
            somme += (entry[0] - entry[1]) ** 2

        resultats[name] = somme / len(values)

    return resultats


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
