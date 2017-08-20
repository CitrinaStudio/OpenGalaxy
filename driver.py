import os

from numpy import random as nprand
from cassandra.cluster import Cluster

import gen


CLUSTER = Cluster()
SESSION = CLUSTER.connect('galaxy_0')

def execute_cqlsh(query):
    if query != "":
        os.system("cqlsh -e \"%s\"" % query)

def check_record_exist(obj_type, keyspace_name, poz, coor_upper_bound):

    query = int(list(list(SESSION.execute("""SELECT count(*) FROM %s.%s WHERE id='%s';""" % (keyspace_name, obj_type, gen.gen_crc32_hash(poz)) )) [0]) [0])

    if query == 1:

        print("/|\\")
        tumbler = 0

        while tumbler == 0:
            print("/|\\")

            x = round(nprand.uniform(-coor_upper_bound, coor_upper_bound), 2)
            y = round(nprand.uniform(-coor_upper_bound, coor_upper_bound), 2)
            z = round(nprand.uniform(-coor_upper_bound, coor_upper_bound), 2)
            poz = (x, y, z)



            query = int(list(list(SESSION.execute("""SELECT count(*) FROM %s.%s WHERE id='%s';""" % (keyspace_name, obj_type, gen.gen_crc32_hash(poz)) )) [0]) [0])

            if query == 0:
                tumbler = 1
    
    return poz
    
