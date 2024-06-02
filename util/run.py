import argparse
import json
import sys
import conf
import terminal

def main():
    # Load Config
    config = conf.load('run-conf.json')
    
    # Arg manager
    parser = argparse.ArgumentParser(description='Launch shortcut form config file')
    subparsers = parser.add_subparsers(help='Shortcut category', dest='category')
    
    for category in config:
        parser_a = subparsers.add_parser(category, formatter_class=argparse.RawTextHelpFormatter)
        parser_a.add_argument(
            'key',
            choices=config[category].keys(),
            type=str,   
            help="Shortcut key and command associated: \n " + (json.dumps(config[category]).replace(",", ",\n").replace("{", "").replace("}", ""))
        )        
    
    args = parser.parse_args()
    if args.category is None:
        parser.print_help(sys.stderr)
        exit()
        
    # Run shortcut cmd
    terminal.cmd(config[args.category][args.key])
    
if __name__ == "__main__":
    main()