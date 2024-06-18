import argparse
import json
import sys
import conf
import string_util
import terminal

def main():
    # Load Config
    config = conf.load('run-conf.json')
    
    # Arg manager
    parser = argparse.ArgumentParser(description='Launch shortcut from config file')
    subparsers = parser.add_subparsers(help='Shortcut category', dest='category')
    
    for category in config:
        parser_a = subparsers.add_parser(category, formatter_class=argparse.RawTextHelpFormatter)
        parser_a.add_argument(
            'key',
            choices=config[category].keys(),
            type=str,   
            help="Shortcut key and command associated: \n " + string_util.dictionnaryToString(config[category])
        )        
    
    args = parser.parse_args()
    if args.category is None:
        parser.print_help(sys.stderr)
        exit()
        
    # Run shortcut cmd
    terminal.cmd(config[args.category][args.key])
    
if __name__ == "__main__":
    main()