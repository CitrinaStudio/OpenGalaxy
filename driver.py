import os
import sqlite3 as sqlite

from numpy import random as nprand
from cassandra.cluster import Cluster


import gen


CLUSTER = Cluster()
SESSION = CLUSTER.connect('galaxy_0')

connect = sqlite.connect("space.db")
db = connect.cursor()

def execute_cqlsh(query):
    if query != "":
        os.system("cqlsh -e \"%s\"" % query)

def execute_sqlite(query):
    if query != "":
        os.system("sqlite3 ./space.db \"%s\"" %  query)

def check_record_exist(keyspace_name, poz, coor_upper_bound):

    query = int(list(list(SESSION.execute("""SELECT count(*) FROM %s.space WHERE id='%s';""" % (keyspace_name, gen.gen_crc32_hash(poz)) )) [0]) [0])

    if query == 1:

        print("/|\\")
        tumbler = 0

        while tumbler == 0:
            print("/|\\")

            x = nprand.uniform(-coor_upper_bound, coor_upper_bound)
            y = nprand.uniform(-coor_upper_bound, coor_upper_bound)
            z = nprand.uniform(-coor_upper_bound, coor_upper_bound)
            poz = (x, y, z)



            query = int(list(list(SESSION.execute("""SELECT count(*) FROM %s.space WHERE id='%s';""" % (keyspace_name, gen.gen_crc32_hash(poz)) )) [0]) [0])

            if query == 0:
                tumbler = 1
    
    return poz
    
def check_record_exist_sqlite(obj_type, poz, coor_upper_bound):
    

    query = tuple(db.execute("""SELECT count(*) FROM %s WHERE id='%s';""" % (obj_type, gen.gen_crc32_hash(poz))))[0][0]

    if query == 1:
    
        print("/|\\")
        tumbler = 0

        while tumbler == 0:
            print("/|\\")

            x = nprand.uniform(-coor_upper_bound, coor_upper_bound)
            y = nprand.uniform(-coor_upper_bound, coor_upper_bound)
            z = nprand.uniform(-coor_upper_bound, coor_upper_bound)
            poz = (x, y, z)



            query = tuple(db.execute("""SELECT count(*) FROM %s WHERE id='%s';""" % (obj_type, gen.gen_crc32_hash(poz))))[0][0]

            if query == 0:
                tumbler = 1
    
    return poz
        