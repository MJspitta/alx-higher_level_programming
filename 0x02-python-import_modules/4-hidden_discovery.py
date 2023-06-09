#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    name_mods = dir(hidden_4)
    for name in name_mods:
        if name[:2] != '__':
            print(name)
