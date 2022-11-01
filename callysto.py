#!/usr/bin/env python
import argparse
import sys
from os import path

from workflow import Workflow


def parse_command_line(argv):
    parser = argparse.ArgumentParser(
        prog="Callysto",
        description="Linear workflow runner",
        epilog="foo"
    )
    parser.add_argument('filename', help='the name of the YAML file containing the workflow definition to execute')
    parser.add_argument('-s', '--state-file', help="The name of the file to save the execution results in. If the " +
                                                   "file already exists, this will fail unless --force or --resume "
                                                   "is also specified.")
    parser.add_argument('-f', '--force', action='store_true', help="Force overwriting an existing state file.")
    return parser.parse_args(argv)


def run_workflow(args):
    workflow = Workflow.from_file(args.filename)
    if args.state_file:
        workflow.with_state_file(args.state_file)
    print(workflow.run())


if __name__ == '__main__':
    arguments = parse_command_line(sys.argv[1:])
    if arguments.force and not arguments.state_file:
        print("Cannot specify --force without --state-file")
        exit(1)
    if not arguments.force and arguments.state_file and path.exists(arguments.state_file):
        print(f"State file {arguments.state_file} already exists. If you want to overwrite it, also specify --force.")
        exit(1)
    run_workflow(arguments)

