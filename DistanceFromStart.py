import re

def main():
    directions = input("Directions: ")
    each_position = directions.split(",")
    final_directions = ''
    for d in each_position:
        m = re.split('(\d+)', d)
        final_directions = final_directions + (m[0] * int(m[1]))

    print(final_directions)


if __name__ == '__main__':
    main()