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

    elif type == "meteorites":
        gen.gen_meteorites(int(sys.argv[2]), float(sys.argv[3]))

    elif type == "blackhole":
        gen.gen_blackhole(int(sys.argv[2]), float(sys.argv[3]))     
    
    elif type == "nebula":
        gen.gen_nebula(int(sys.argv[2]), float(sys.argv[3]))   
    
    elif type == "all":
        gen.gen_stars(int(sys.argv[2]), float(sys.argv[3]))
        gen.gen_comets(int(sys.argv[2]), float(sys.argv[3]))
        gen.gen_planets(int(sys.argv[2]), float(sys.argv[3]))
        gen.gen_meteorites(int(sys.argv[2]), float(sys.argv[3]))
        gen.gen_blackhole(int(sys.argv[2]), float(sys.argv[3])) 
        gen.gen_nebula(int(sys.argv[2]), float(sys.argv[3]))
    
    
    else:
        print("%s type is not defined" % type)
        exit(1)

if __name__ == "__main__":
    main()
