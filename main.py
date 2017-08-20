import sys

import gen

def main():
    type = sys.argv[1]
    print(sys.argv)
    
    if type == "planets":
        gen.gen_planets(int(sys.argv[2]), int(sys.argv[3]))

    elif type == "comets":
        gen.gen_comets(int(sys.argv[2]), int(sys.argv[3]))
    
    elif type == "stars":
        gen.gen_stars(int(sys.argv[2]), int(sys.argv[3]))
    
    else:
        print("%s type is not defined" % type)
        exit(1)

if __name__ == "__main__":
    main()