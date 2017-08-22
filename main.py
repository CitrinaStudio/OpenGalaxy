# Copyright (c) 2017 phonphey
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys

import gen

def main():
    type = sys.argv[1]
    
    if type == "planets":
        gen.gen_planets(int(sys.argv[2]), float(sys.argv[3]))

    elif type == "comets":
        gen.gen_comets(int(sys.argv[2]), float(sys.argv[3]))
    
    elif type == "stars":
        gen.gen_stars(int(sys.argv[2]), float(sys.argv[3]))
    
    elif type == "all":
        gen.gen_stars(int(sys.argv[2]), float(sys.argv[3]))
        gen.gen_comets(int(sys.argv[2]), float(sys.argv[3]))
        gen.gen_planets(int(sys.argv[2]), float(sys.argv[3]))
    
    else:
        print("%s type is not defined" % type)
        exit(1)

if __name__ == "__main__":
    main()