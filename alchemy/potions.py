#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/29 22:42:25 by marasolo            #+#    #+#            #
#   Updated: 2026/06/30 09:12:49 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    return ("Healing potion brewed with ’[created earth element]’ " +
            "and ’[created air element]")


def strength_potion() -> str:
    return ("Strength potion brewed with ’[created fire element]’ " +
            "and ’[created water element]")
