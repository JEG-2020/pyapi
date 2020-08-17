#!/usr/bin/python3

import json

def main():
    hitchikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchikers)

    jsonstring = json.dumps(hitchikers)
    print(jsonstring)


if __name__ == "__main__":
    main()


