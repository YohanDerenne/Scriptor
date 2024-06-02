#!/usr/bin/env python3
import argparse
import conf
import terminal

# Load Config
config = conf.load('dock-conf.json')

def main():    
    # Arg manager
    parser = argparse.ArgumentParser(description="Docker exec shortcut")
    parser.add_argument(
        'name',
        choices=config.keys(),
        type=str,
        help='Container name'
    )
    
    args = parser.parse_args()
    terminal.cmd(config[args.name])

if __name__ == '__main__':
    main()
