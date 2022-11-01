import argparse
import sys

from workflow import Workflow


def parse_command_line(argv):
    parser = argparse.ArgumentParser(
        prog="Callysto",
        description="Linear workflow runner",
        epilog="foo"
    )
    parser.add_argument('filename', help='the name of the YAML file containing the workflow definition to execute')
    return parser.parse_args(argv)


def run_workflow(file_name):
    Workflow.from_file(args.filename).run()


if __name__ == '__main__':
    args = parse_command_line(sys.argv[1:])
    run_workflow(args.filename)
