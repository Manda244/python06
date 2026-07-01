#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_0.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/30 09:15:34 by marasolo            #+#    #+#            #
#   Updated: 2026/06/30 09:24:18 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.potions import create_air, create_earth, create_fire, create_water


print("=== Distillation 0 ===")
print("Direct access to alchemy/potions.py")
print("Testing strength_potion: Strength potion brewed with  "
      f"'{create_fire()}' and '{create_water()}'")
print("Testing healing_potion:  Healing potion brewed with "
      f"'{create_earth()}' and '{create_air()}'")
