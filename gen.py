# Copyright (c) 2017 phonphey
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

""""Object generator"""

import random
import string
import zlib


from numpy import random as nprand


import driver


def gen_crc32_hash(params):
    id = str(hex(zlib.crc32(str(params).encode("utf-8"))).split('x')[-1])

    return id


def gen_name(size):
    tumbler = nprand.randint(1, 3)
    if tumbler == 1:
        return string.capwords(''.join(random.choice(string.ascii_uppercase) for _ in range(size)))
    else:
        return string.capwords(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size)))


def gen_id(params):
    return zlib.adler32(str(params).encode('utf-8'))


def gen_stars(count, coor_upper_bound):
    queris_pool = ""
    queris_in_pool = 0

    for i in range(0, count, 1):
        star_name = gen_name(random.randint(5, 9))
        star_temp = random.uniform(2000, 60000)

        x = nprand.uniform(-coor_upper_bound, coor_upper_bound)
        y = nprand.uniform(-coor_upper_bound, coor_upper_bound)
        z = nprand.uniform(-coor_upper_bound, coor_upper_bound)

        poz = (x, y, z)

        id = gen_crc32_hash(poz)

        if 2000 <= star_temp <= 3500:
            star_color = "red"
            star_weight = random.uniform(0.3, 0.8)
            star_radius = random.uniform(0.4, 0.9)
            star_luminosity = random.uniform(0.04, 0.4)

        elif 3500 <= star_temp <= 5000:
            star_color = "orange"
            star_weight = random.uniform(0.8, 1.1)
            star_radius = random.uniform(0.9, 1.1)
            star_luminosity = random.uniform(0.4, 1.2)

        elif 5000 <= star_temp <= 6000:
            star_color = "yellow"
            star_weight = random.uniform(1.1, 1.7)
            star_radius = random.uniform(1.1, 1.3)
            star_luminosity = random.uniform(1.2, 6)

        elif 6000 <= star_temp <= 7500:
            star_color = "yellow-white"
            star_weight = random.uniform(1.7, 3.1)
            star_radius = random.uniform(1.3, 2.1)
            star_luminosity = random.uniform(6, 80)

        elif 7500 <= star_temp <= 10000:
            star_color = "white"
            star_weight = random.uniform(3.1, 18)
            star_radius = random.uniform(2.1, 7)
            star_luminosity = random.uniform(80, 20000)

        elif 10000 <= star_temp <= 30000:
            star_color = "white-blue"
            star_weight = random.uniform(18, 60)
            star_radius = random.uniform(7, 15)
            star_luminosity = random.uniform(20000, 1400000)

        elif 30000 <= star_temp <= 60000:
            star_color = "blue"
            star_weight = random.uniform(60, 80)
            star_radius = random.uniform(15, 20)
            star_luminosity = random.uniform(1400000, 2500000)

        poz = driver.check_record_exist(
            "galaxy_0", poz, coor_upper_bound)

        queris_pool += "INSERT INTO galaxy_0.space (id, color, type, luminosity, name, radius, temp, weight, x, y, z) VALUES ('%s', '%s', '%s', %f, '%s', %f, %f, %f, %f, %f, %f); " % (
            id, star_color, "star", star_luminosity, star_name, star_radius, star_temp, star_weight, poz[0], poz[1], poz[2])

        queris_in_pool += 1

        if queris_in_pool >= 1000:
            queris_in_pool = 0
            driver.execute_cqlsh(queris_pool)
            queris_pool = ""

    driver.execute_cqlsh(queris_pool)

def gen_planets(count, coor_upper_bound):
    queris_pool = ""
    queris_in_pool = 0

    for i in range(0, count, 1):
        planet_name = gen_name(random.randint(1, 5))
        planet_weight = random.uniform(0.0002, 317.8)
        planet_radius = random.uniform(0.0592, 11.209) / 2

        x = nprand.uniform(-coor_upper_bound, coor_upper_bound)
        y = nprand.uniform(-coor_upper_bound, coor_upper_bound)
        z = nprand.uniform(-coor_upper_bound, coor_upper_bound)

        poz = (x, y, z)

        poz = driver.check_record_exist(
            "galaxy_0", poz, coor_upper_bound)

        id = gen_crc32_hash(poz)

        queris_pool += "INSERT INTO galaxy_0.space (id, name, type, radius, weight, x, y, z) VALUES ('%s', '%s', '%s', %s, %s, %s, %s, %s); " % (
            id, planet_name, "planet", planet_radius, planet_weight, poz[0], poz[1], poz[2])

        queris_in_pool += 1

        if queris_in_pool >= 1000:
            queris_in_pool = 0
            driver.execute_cqlsh(queris_pool)
            queris_pool = ""

    driver.execute_cqlsh(queris_pool)


def gen_comets(count, coor_upper_bound):
    queris_pool = ""
    queris_in_pool = 0

    for i in range(0, count, 1):
        comet_name = gen_name(random.randint(3, 6))
        comet_weight = random.uniform(2200000000000, 220000000000000)

        x = nprand.uniform(-coor_upper_bound, coor_upper_bound)
        y = nprand.uniform(-coor_upper_bound, coor_upper_bound)
        z = nprand.uniform(-coor_upper_bound, coor_upper_bound)

        poz = (x, y, z)

        poz = poz = driver.check_record_exist(
            "galaxy_0", poz, coor_upper_bound)

        id = gen_crc32_hash(poz)
        queris_pool += "INSERT INTO galaxy_0.space (id, name, type, weight, x, y, z) VALUES ('%s', '%s', '%s', %s, %s, %s, %s); " % (
            id, comet_name, "comet", comet_weight, poz[0], poz[1], poz[2])

        queris_in_pool += 1

        if queris_in_pool >= 1000:
            queris_in_pool = 0
            driver.execute_cqlsh(queris_pool)
            queris_pool = ""

    driver.execute_cqlsh(queris_pool)
