

#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 Ontology design facility
===============================================================================

This program is part of the ProcessModelling suite

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "16.09.2019"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "5.04"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"


import sys
import os

ProMo_path = os.path.join("../../","ProMo")



root = os.path.abspath(ProMo_path)      #os.path.join("../../"{{ProMo}}) #ProcessModeller_v7_04"))

ext = [root, os.path.join(root, 'packages'), \
             os.path.join(root, 'tasks'), \
             os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration')
       ]
# print(os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration'))

# emmo = "/home/heinz/1_Gits/ProcessModeller/ProcessModeller_v7_04/packages/OntologyBuilder/EMMO_Integration/"

sys.path.extend(ext)
from OntologyBuilder.EMMO_Integration.emmo_attach import ProMoOwlOntology
from Common.ontology_container import OntologyContainer

from owlready2 import *

ontology = OntologyContainer("ProMo_sandbox2") #'flash_03')


variables = ontology.variables

name = "play"
owlfile = name+".owl"

# onto  = O.setup_ontology(name)
o = ProMoOwlOntology()
onto = o.setupOnto()

with onto:
  class ProMoVar(onto.VAR):
    pass

  class has_function(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

  class function(Thing):
    domain  = [ProMoVar]
    range   = [ProMoVar]
    pass

  class is_function_of(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

# 1
label = variables[1]["label"]
network = variables[1]["network"]
variable_type = variables[1]["type"]
label = variables[1]["label"]
doc = variables[1]["doc"]
onto_ID = "V_1"
V_1 = onto.ProMoVar( onto_ID )
V_1.label = label
V_1.network = network
V_1.variable_type = variable_type
V_1.comment = doc

units = variables[1]["units"].asList()
V_1.time = [ units[0] ]
V_1.length = [ units[1] ]
V_1.amount = [ units[2] ]
V_1.mass = [ units[3] ]
V_1.temperature = [ units[4] ]
V_1.current = [ units[5] ]
V_1.light = [ units[6] ]

# 3
label = variables[3]["label"]
network = variables[3]["network"]
variable_type = variables[3]["type"]
label = variables[3]["label"]
doc = variables[3]["doc"]
onto_ID = "V_3"
V_3 = onto.ProMoVar( onto_ID )
V_3.label = label
V_3.network = network
V_3.variable_type = variable_type
V_3.comment = doc

units = variables[3]["units"].asList()
V_3.time = [ units[0] ]
V_3.length = [ units[1] ]
V_3.amount = [ units[2] ]
V_3.mass = [ units[3] ]
V_3.temperature = [ units[4] ]
V_3.current = [ units[5] ]
V_3.light = [ units[6] ]

# 4
label = variables[4]["label"]
network = variables[4]["network"]
variable_type = variables[4]["type"]
label = variables[4]["label"]
doc = variables[4]["doc"]
onto_ID = "V_4"
V_4 = onto.ProMoVar( onto_ID )
V_4.label = label
V_4.network = network
V_4.variable_type = variable_type
V_4.comment = doc

units = variables[4]["units"].asList()
V_4.time = [ units[0] ]
V_4.length = [ units[1] ]
V_4.amount = [ units[2] ]
V_4.mass = [ units[3] ]
V_4.temperature = [ units[4] ]
V_4.current = [ units[5] ]
V_4.light = [ units[6] ]

# 5
label = variables[5]["label"]
network = variables[5]["network"]
variable_type = variables[5]["type"]
label = variables[5]["label"]
doc = variables[5]["doc"]
onto_ID = "V_5"
V_5 = onto.ProMoVar( onto_ID )
V_5.label = label
V_5.network = network
V_5.variable_type = variable_type
V_5.comment = doc

units = variables[5]["units"].asList()
V_5.time = [ units[0] ]
V_5.length = [ units[1] ]
V_5.amount = [ units[2] ]
V_5.mass = [ units[3] ]
V_5.temperature = [ units[4] ]
V_5.current = [ units[5] ]
V_5.light = [ units[6] ]

# 6
label = variables[6]["label"]
network = variables[6]["network"]
variable_type = variables[6]["type"]
label = variables[6]["label"]
doc = variables[6]["doc"]
onto_ID = "V_6"
V_6 = onto.ProMoVar( onto_ID )
V_6.label = label
V_6.network = network
V_6.variable_type = variable_type
V_6.comment = doc

units = variables[6]["units"].asList()
V_6.time = [ units[0] ]
V_6.length = [ units[1] ]
V_6.amount = [ units[2] ]
V_6.mass = [ units[3] ]
V_6.temperature = [ units[4] ]
V_6.current = [ units[5] ]
V_6.light = [ units[6] ]

# 7
label = variables[7]["label"]
network = variables[7]["network"]
variable_type = variables[7]["type"]
label = variables[7]["label"]
doc = variables[7]["doc"]
onto_ID = "V_7"
V_7 = onto.ProMoVar( onto_ID )
V_7.label = label
V_7.network = network
V_7.variable_type = variable_type
V_7.comment = doc

units = variables[7]["units"].asList()
V_7.time = [ units[0] ]
V_7.length = [ units[1] ]
V_7.amount = [ units[2] ]
V_7.mass = [ units[3] ]
V_7.temperature = [ units[4] ]
V_7.current = [ units[5] ]
V_7.light = [ units[6] ]

# 8
label = variables[8]["label"]
network = variables[8]["network"]
variable_type = variables[8]["type"]
label = variables[8]["label"]
doc = variables[8]["doc"]
onto_ID = "V_8"
V_8 = onto.ProMoVar( onto_ID )
V_8.label = label
V_8.network = network
V_8.variable_type = variable_type
V_8.comment = doc

units = variables[8]["units"].asList()
V_8.time = [ units[0] ]
V_8.length = [ units[1] ]
V_8.amount = [ units[2] ]
V_8.mass = [ units[3] ]
V_8.temperature = [ units[4] ]
V_8.current = [ units[5] ]
V_8.light = [ units[6] ]

# 9
label = variables[9]["label"]
network = variables[9]["network"]
variable_type = variables[9]["type"]
label = variables[9]["label"]
doc = variables[9]["doc"]
onto_ID = "V_9"
V_9 = onto.ProMoVar( onto_ID )
V_9.label = label
V_9.network = network
V_9.variable_type = variable_type
V_9.comment = doc

units = variables[9]["units"].asList()
V_9.time = [ units[0] ]
V_9.length = [ units[1] ]
V_9.amount = [ units[2] ]
V_9.mass = [ units[3] ]
V_9.temperature = [ units[4] ]
V_9.current = [ units[5] ]
V_9.light = [ units[6] ]

# 10
label = variables[10]["label"]
network = variables[10]["network"]
variable_type = variables[10]["type"]
label = variables[10]["label"]
doc = variables[10]["doc"]
onto_ID = "V_10"
V_10 = onto.ProMoVar( onto_ID )
V_10.label = label
V_10.network = network
V_10.variable_type = variable_type
V_10.comment = doc

units = variables[10]["units"].asList()
V_10.time = [ units[0] ]
V_10.length = [ units[1] ]
V_10.amount = [ units[2] ]
V_10.mass = [ units[3] ]
V_10.temperature = [ units[4] ]
V_10.current = [ units[5] ]
V_10.light = [ units[6] ]

# 11
label = variables[11]["label"]
network = variables[11]["network"]
variable_type = variables[11]["type"]
label = variables[11]["label"]
doc = variables[11]["doc"]
onto_ID = "V_11"
V_11 = onto.ProMoVar( onto_ID )
V_11.label = label
V_11.network = network
V_11.variable_type = variable_type
V_11.comment = doc

units = variables[11]["units"].asList()
V_11.time = [ units[0] ]
V_11.length = [ units[1] ]
V_11.amount = [ units[2] ]
V_11.mass = [ units[3] ]
V_11.temperature = [ units[4] ]
V_11.current = [ units[5] ]
V_11.light = [ units[6] ]

# 12
label = variables[12]["label"]
network = variables[12]["network"]
variable_type = variables[12]["type"]
label = variables[12]["label"]
doc = variables[12]["doc"]
onto_ID = "V_12"
V_12 = onto.ProMoVar( onto_ID )
V_12.label = label
V_12.network = network
V_12.variable_type = variable_type
V_12.comment = doc

units = variables[12]["units"].asList()
V_12.time = [ units[0] ]
V_12.length = [ units[1] ]
V_12.amount = [ units[2] ]
V_12.mass = [ units[3] ]
V_12.temperature = [ units[4] ]
V_12.current = [ units[5] ]
V_12.light = [ units[6] ]

# 13
label = variables[13]["label"]
network = variables[13]["network"]
variable_type = variables[13]["type"]
label = variables[13]["label"]
doc = variables[13]["doc"]
onto_ID = "V_13"
V_13 = onto.ProMoVar( onto_ID )
V_13.label = label
V_13.network = network
V_13.variable_type = variable_type
V_13.comment = doc

units = variables[13]["units"].asList()
V_13.time = [ units[0] ]
V_13.length = [ units[1] ]
V_13.amount = [ units[2] ]
V_13.mass = [ units[3] ]
V_13.temperature = [ units[4] ]
V_13.current = [ units[5] ]
V_13.light = [ units[6] ]

# 14
label = variables[14]["label"]
network = variables[14]["network"]
variable_type = variables[14]["type"]
label = variables[14]["label"]
doc = variables[14]["doc"]
onto_ID = "V_14"
V_14 = onto.ProMoVar( onto_ID )
V_14.label = label
V_14.network = network
V_14.variable_type = variable_type
V_14.comment = doc

units = variables[14]["units"].asList()
V_14.time = [ units[0] ]
V_14.length = [ units[1] ]
V_14.amount = [ units[2] ]
V_14.mass = [ units[3] ]
V_14.temperature = [ units[4] ]
V_14.current = [ units[5] ]
V_14.light = [ units[6] ]

# 15
label = variables[15]["label"]
network = variables[15]["network"]
variable_type = variables[15]["type"]
label = variables[15]["label"]
doc = variables[15]["doc"]
onto_ID = "V_15"
V_15 = onto.ProMoVar( onto_ID )
V_15.label = label
V_15.network = network
V_15.variable_type = variable_type
V_15.comment = doc

units = variables[15]["units"].asList()
V_15.time = [ units[0] ]
V_15.length = [ units[1] ]
V_15.amount = [ units[2] ]
V_15.mass = [ units[3] ]
V_15.temperature = [ units[4] ]
V_15.current = [ units[5] ]
V_15.light = [ units[6] ]

# 16
label = variables[16]["label"]
network = variables[16]["network"]
variable_type = variables[16]["type"]
label = variables[16]["label"]
doc = variables[16]["doc"]
onto_ID = "V_16"
V_16 = onto.ProMoVar( onto_ID )
V_16.label = label
V_16.network = network
V_16.variable_type = variable_type
V_16.comment = doc

units = variables[16]["units"].asList()
V_16.time = [ units[0] ]
V_16.length = [ units[1] ]
V_16.amount = [ units[2] ]
V_16.mass = [ units[3] ]
V_16.temperature = [ units[4] ]
V_16.current = [ units[5] ]
V_16.light = [ units[6] ]

# 17
label = variables[17]["label"]
network = variables[17]["network"]
variable_type = variables[17]["type"]
label = variables[17]["label"]
doc = variables[17]["doc"]
onto_ID = "V_17"
V_17 = onto.ProMoVar( onto_ID )
V_17.label = label
V_17.network = network
V_17.variable_type = variable_type
V_17.comment = doc

units = variables[17]["units"].asList()
V_17.time = [ units[0] ]
V_17.length = [ units[1] ]
V_17.amount = [ units[2] ]
V_17.mass = [ units[3] ]
V_17.temperature = [ units[4] ]
V_17.current = [ units[5] ]
V_17.light = [ units[6] ]

# 18
label = variables[18]["label"]
network = variables[18]["network"]
variable_type = variables[18]["type"]
label = variables[18]["label"]
doc = variables[18]["doc"]
onto_ID = "V_18"
V_18 = onto.ProMoVar( onto_ID )
V_18.label = label
V_18.network = network
V_18.variable_type = variable_type
V_18.comment = doc

units = variables[18]["units"].asList()
V_18.time = [ units[0] ]
V_18.length = [ units[1] ]
V_18.amount = [ units[2] ]
V_18.mass = [ units[3] ]
V_18.temperature = [ units[4] ]
V_18.current = [ units[5] ]
V_18.light = [ units[6] ]

# 19
label = variables[19]["label"]
network = variables[19]["network"]
variable_type = variables[19]["type"]
label = variables[19]["label"]
doc = variables[19]["doc"]
onto_ID = "V_19"
V_19 = onto.ProMoVar( onto_ID )
V_19.label = label
V_19.network = network
V_19.variable_type = variable_type
V_19.comment = doc

units = variables[19]["units"].asList()
V_19.time = [ units[0] ]
V_19.length = [ units[1] ]
V_19.amount = [ units[2] ]
V_19.mass = [ units[3] ]
V_19.temperature = [ units[4] ]
V_19.current = [ units[5] ]
V_19.light = [ units[6] ]

# 20
label = variables[20]["label"]
network = variables[20]["network"]
variable_type = variables[20]["type"]
label = variables[20]["label"]
doc = variables[20]["doc"]
onto_ID = "V_20"
V_20 = onto.ProMoVar( onto_ID )
V_20.label = label
V_20.network = network
V_20.variable_type = variable_type
V_20.comment = doc

units = variables[20]["units"].asList()
V_20.time = [ units[0] ]
V_20.length = [ units[1] ]
V_20.amount = [ units[2] ]
V_20.mass = [ units[3] ]
V_20.temperature = [ units[4] ]
V_20.current = [ units[5] ]
V_20.light = [ units[6] ]

# 21
label = variables[21]["label"]
network = variables[21]["network"]
variable_type = variables[21]["type"]
label = variables[21]["label"]
doc = variables[21]["doc"]
onto_ID = "V_21"
V_21 = onto.ProMoVar( onto_ID )
V_21.label = label
V_21.network = network
V_21.variable_type = variable_type
V_21.comment = doc

units = variables[21]["units"].asList()
V_21.time = [ units[0] ]
V_21.length = [ units[1] ]
V_21.amount = [ units[2] ]
V_21.mass = [ units[3] ]
V_21.temperature = [ units[4] ]
V_21.current = [ units[5] ]
V_21.light = [ units[6] ]

# 22
label = variables[22]["label"]
network = variables[22]["network"]
variable_type = variables[22]["type"]
label = variables[22]["label"]
doc = variables[22]["doc"]
onto_ID = "V_22"
V_22 = onto.ProMoVar( onto_ID )
V_22.label = label
V_22.network = network
V_22.variable_type = variable_type
V_22.comment = doc

units = variables[22]["units"].asList()
V_22.time = [ units[0] ]
V_22.length = [ units[1] ]
V_22.amount = [ units[2] ]
V_22.mass = [ units[3] ]
V_22.temperature = [ units[4] ]
V_22.current = [ units[5] ]
V_22.light = [ units[6] ]

# 23
label = variables[23]["label"]
network = variables[23]["network"]
variable_type = variables[23]["type"]
label = variables[23]["label"]
doc = variables[23]["doc"]
onto_ID = "V_23"
V_23 = onto.ProMoVar( onto_ID )
V_23.label = label
V_23.network = network
V_23.variable_type = variable_type
V_23.comment = doc

units = variables[23]["units"].asList()
V_23.time = [ units[0] ]
V_23.length = [ units[1] ]
V_23.amount = [ units[2] ]
V_23.mass = [ units[3] ]
V_23.temperature = [ units[4] ]
V_23.current = [ units[5] ]
V_23.light = [ units[6] ]

# 24
label = variables[24]["label"]
network = variables[24]["network"]
variable_type = variables[24]["type"]
label = variables[24]["label"]
doc = variables[24]["doc"]
onto_ID = "V_24"
V_24 = onto.ProMoVar( onto_ID )
V_24.label = label
V_24.network = network
V_24.variable_type = variable_type
V_24.comment = doc

units = variables[24]["units"].asList()
V_24.time = [ units[0] ]
V_24.length = [ units[1] ]
V_24.amount = [ units[2] ]
V_24.mass = [ units[3] ]
V_24.temperature = [ units[4] ]
V_24.current = [ units[5] ]
V_24.light = [ units[6] ]

# 25
label = variables[25]["label"]
network = variables[25]["network"]
variable_type = variables[25]["type"]
label = variables[25]["label"]
doc = variables[25]["doc"]
onto_ID = "V_25"
V_25 = onto.ProMoVar( onto_ID )
V_25.label = label
V_25.network = network
V_25.variable_type = variable_type
V_25.comment = doc

units = variables[25]["units"].asList()
V_25.time = [ units[0] ]
V_25.length = [ units[1] ]
V_25.amount = [ units[2] ]
V_25.mass = [ units[3] ]
V_25.temperature = [ units[4] ]
V_25.current = [ units[5] ]
V_25.light = [ units[6] ]

# 26
label = variables[26]["label"]
network = variables[26]["network"]
variable_type = variables[26]["type"]
label = variables[26]["label"]
doc = variables[26]["doc"]
onto_ID = "V_26"
V_26 = onto.ProMoVar( onto_ID )
V_26.label = label
V_26.network = network
V_26.variable_type = variable_type
V_26.comment = doc

units = variables[26]["units"].asList()
V_26.time = [ units[0] ]
V_26.length = [ units[1] ]
V_26.amount = [ units[2] ]
V_26.mass = [ units[3] ]
V_26.temperature = [ units[4] ]
V_26.current = [ units[5] ]
V_26.light = [ units[6] ]

# 27
label = variables[27]["label"]
network = variables[27]["network"]
variable_type = variables[27]["type"]
label = variables[27]["label"]
doc = variables[27]["doc"]
onto_ID = "V_27"
V_27 = onto.ProMoVar( onto_ID )
V_27.label = label
V_27.network = network
V_27.variable_type = variable_type
V_27.comment = doc

units = variables[27]["units"].asList()
V_27.time = [ units[0] ]
V_27.length = [ units[1] ]
V_27.amount = [ units[2] ]
V_27.mass = [ units[3] ]
V_27.temperature = [ units[4] ]
V_27.current = [ units[5] ]
V_27.light = [ units[6] ]

# 28
label = variables[28]["label"]
network = variables[28]["network"]
variable_type = variables[28]["type"]
label = variables[28]["label"]
doc = variables[28]["doc"]
onto_ID = "V_28"
V_28 = onto.ProMoVar( onto_ID )
V_28.label = label
V_28.network = network
V_28.variable_type = variable_type
V_28.comment = doc

units = variables[28]["units"].asList()
V_28.time = [ units[0] ]
V_28.length = [ units[1] ]
V_28.amount = [ units[2] ]
V_28.mass = [ units[3] ]
V_28.temperature = [ units[4] ]
V_28.current = [ units[5] ]
V_28.light = [ units[6] ]

# 29
label = variables[29]["label"]
network = variables[29]["network"]
variable_type = variables[29]["type"]
label = variables[29]["label"]
doc = variables[29]["doc"]
onto_ID = "V_29"
V_29 = onto.ProMoVar( onto_ID )
V_29.label = label
V_29.network = network
V_29.variable_type = variable_type
V_29.comment = doc

units = variables[29]["units"].asList()
V_29.time = [ units[0] ]
V_29.length = [ units[1] ]
V_29.amount = [ units[2] ]
V_29.mass = [ units[3] ]
V_29.temperature = [ units[4] ]
V_29.current = [ units[5] ]
V_29.light = [ units[6] ]

# 30
label = variables[30]["label"]
network = variables[30]["network"]
variable_type = variables[30]["type"]
label = variables[30]["label"]
doc = variables[30]["doc"]
onto_ID = "V_30"
V_30 = onto.ProMoVar( onto_ID )
V_30.label = label
V_30.network = network
V_30.variable_type = variable_type
V_30.comment = doc

units = variables[30]["units"].asList()
V_30.time = [ units[0] ]
V_30.length = [ units[1] ]
V_30.amount = [ units[2] ]
V_30.mass = [ units[3] ]
V_30.temperature = [ units[4] ]
V_30.current = [ units[5] ]
V_30.light = [ units[6] ]

# 31
label = variables[31]["label"]
network = variables[31]["network"]
variable_type = variables[31]["type"]
label = variables[31]["label"]
doc = variables[31]["doc"]
onto_ID = "V_31"
V_31 = onto.ProMoVar( onto_ID )
V_31.label = label
V_31.network = network
V_31.variable_type = variable_type
V_31.comment = doc

units = variables[31]["units"].asList()
V_31.time = [ units[0] ]
V_31.length = [ units[1] ]
V_31.amount = [ units[2] ]
V_31.mass = [ units[3] ]
V_31.temperature = [ units[4] ]
V_31.current = [ units[5] ]
V_31.light = [ units[6] ]

# 32
label = variables[32]["label"]
network = variables[32]["network"]
variable_type = variables[32]["type"]
label = variables[32]["label"]
doc = variables[32]["doc"]
onto_ID = "V_32"
V_32 = onto.ProMoVar( onto_ID )
V_32.label = label
V_32.network = network
V_32.variable_type = variable_type
V_32.comment = doc

units = variables[32]["units"].asList()
V_32.time = [ units[0] ]
V_32.length = [ units[1] ]
V_32.amount = [ units[2] ]
V_32.mass = [ units[3] ]
V_32.temperature = [ units[4] ]
V_32.current = [ units[5] ]
V_32.light = [ units[6] ]

# 33
label = variables[33]["label"]
network = variables[33]["network"]
variable_type = variables[33]["type"]
label = variables[33]["label"]
doc = variables[33]["doc"]
onto_ID = "V_33"
V_33 = onto.ProMoVar( onto_ID )
V_33.label = label
V_33.network = network
V_33.variable_type = variable_type
V_33.comment = doc

units = variables[33]["units"].asList()
V_33.time = [ units[0] ]
V_33.length = [ units[1] ]
V_33.amount = [ units[2] ]
V_33.mass = [ units[3] ]
V_33.temperature = [ units[4] ]
V_33.current = [ units[5] ]
V_33.light = [ units[6] ]

# functions assignments

#1

V_1.has_function = []
#3

V_3.has_function = []
#4

V_4.has_function = []
incidence_list = []
incidence_list.append( V_3 )
incidence_list.append( V_3 )
F_ID = "F_1"
F_1 = onto.function( F_ID )
F_1.is_function_of = incidence_list
V_4.has_function.append( F_1 )
#5

V_5.has_function = []
incidence_list = []
incidence_list.append( V_3 )
incidence_list.append( V_3 )
F_ID = "F_2"
F_2 = onto.function( F_ID )
F_2.is_function_of = incidence_list
V_5.has_function.append( F_2 )
#6

V_6.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_3 )
F_ID = "F_3"
F_3 = onto.function( F_ID )
F_3.is_function_of = incidence_list
V_6.has_function.append( F_3 )
#7

V_7.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_3 )
F_ID = "F_4"
F_4 = onto.function( F_ID )
F_4.is_function_of = incidence_list
V_7.has_function.append( F_4 )
#8

V_8.has_function = []
#9

V_9.has_function = []
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_1 )
incidence_list.append( V_6 )
incidence_list.append( V_7 )
incidence_list.append( V_11 )
F_ID = "F_20"
F_20 = onto.function( F_ID )
F_20.is_function_of = incidence_list
V_9.has_function.append( F_20 )
#10

V_10.has_function = []
incidence_list = []
incidence_list.append( V_30 )
incidence_list.append( V_1 )
incidence_list.append( V_6 )
incidence_list.append( V_7 )
incidence_list.append( V_12 )
F_ID = "F_21"
F_21 = onto.function( F_ID )
F_21.is_function_of = incidence_list
V_10.has_function.append( F_21 )
#11

V_11.has_function = []
incidence_list = []
incidence_list.append( V_9 )
incidence_list.append( V_3 )
F_ID = "F_5"
F_5 = onto.function( F_ID )
F_5.is_function_of = incidence_list
V_11.has_function.append( F_5 )
#12

V_12.has_function = []
incidence_list = []
incidence_list.append( V_10 )
incidence_list.append( V_3 )
F_ID = "F_6"
F_6 = onto.function( F_ID )
F_6.is_function_of = incidence_list
V_12.has_function.append( F_6 )
#13

V_13.has_function = []
#14

V_14.has_function = []
#15

V_15.has_function = []
#16

V_16.has_function = []
#17

V_17.has_function = []
#18

V_18.has_function = []
#19

V_19.has_function = []
#20

V_20.has_function = []
#21

V_21.has_function = []
incidence_list = []
incidence_list.append( V_17 )
incidence_list.append( V_9 )
F_ID = "F_7"
F_7 = onto.function( F_ID )
F_7.is_function_of = incidence_list
V_21.has_function.append( F_7 )
#22

V_22.has_function = []
incidence_list = []
incidence_list.append( V_18 )
incidence_list.append( V_9 )
F_ID = "F_8"
F_8 = onto.function( F_ID )
F_8.is_function_of = incidence_list
V_22.has_function.append( F_8 )
#23

V_23.has_function = []
incidence_list = []
incidence_list.append( V_19 )
incidence_list.append( V_10 )
F_ID = "F_9"
F_9 = onto.function( F_ID )
F_9.is_function_of = incidence_list
V_23.has_function.append( F_9 )
#24

V_24.has_function = []
incidence_list = []
incidence_list.append( V_20 )
incidence_list.append( V_10 )
F_ID = "F_10"
F_10 = onto.function( F_ID )
F_10.is_function_of = incidence_list
V_24.has_function.append( F_10 )
#25

V_25.has_function = []
incidence_list = []
incidence_list.append( V_8 )
incidence_list.append( V_13 )
incidence_list.append( V_8 )
incidence_list.append( V_21 )
F_ID = "F_11"
F_11 = onto.function( F_ID )
F_11.is_function_of = incidence_list
V_25.has_function.append( F_11 )
#26

V_26.has_function = []
incidence_list = []
incidence_list.append( V_8 )
incidence_list.append( V_14 )
incidence_list.append( V_8 )
incidence_list.append( V_22 )
F_ID = "F_12"
F_12 = onto.function( F_ID )
F_12.is_function_of = incidence_list
V_26.has_function.append( F_12 )
#27

V_27.has_function = []
incidence_list = []
incidence_list.append( V_8 )
incidence_list.append( V_15 )
incidence_list.append( V_8 )
incidence_list.append( V_23 )
F_ID = "F_14"
F_14 = onto.function( F_ID )
F_14.is_function_of = incidence_list
V_27.has_function.append( F_14 )
#28

V_28.has_function = []
incidence_list = []
incidence_list.append( V_8 )
incidence_list.append( V_16 )
incidence_list.append( V_8 )
incidence_list.append( V_24 )
F_ID = "F_15"
F_15 = onto.function( F_ID )
F_15.is_function_of = incidence_list
V_28.has_function.append( F_15 )
#29

V_29.has_function = []
incidence_list = []
incidence_list.append( V_25 )
incidence_list.append( V_26 )
F_ID = "F_16"
F_16 = onto.function( F_ID )
F_16.is_function_of = incidence_list
V_29.has_function.append( F_16 )
#30

V_30.has_function = []
incidence_list = []
incidence_list.append( V_27 )
incidence_list.append( V_28 )
F_ID = "F_17"
F_17 = onto.function( F_ID )
F_17.is_function_of = incidence_list
V_30.has_function.append( F_17 )
#31

V_31.has_function = []
incidence_list = []
incidence_list.append( V_21 )
incidence_list.append( V_22 )
F_ID = "F_24"
F_24 = onto.function( F_ID )
F_24.is_function_of = incidence_list
V_31.has_function.append( F_24 )
#32

V_32.has_function = []
incidence_list = []
incidence_list.append( V_23 )
incidence_list.append( V_24 )
F_ID = "F_25"
F_25 = onto.function( F_ID )
F_25.is_function_of = incidence_list
V_32.has_function.append( F_25 )
#33

V_33.has_function = []
incidence_list = []
incidence_list.append( V_31 )
incidence_list.append( V_32 )
F_ID = "F_26"
F_26 = onto.function( F_ID )
F_26.is_function_of = incidence_list
V_33.has_function.append( F_26 )

onto.save("variables.owl")
