from workflow import Workflow


def test_initial_bindings():
    definition = """
bindings:
    firstName: dathan
"""
    workflow = Workflow(definition)
    assert workflow.bindings['firstName'].value == 'dathan'
