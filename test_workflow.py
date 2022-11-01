from workflow import Workflow


def test_initial_bindings():
    definition = """
bindings:
    firstName: dathan
"""
    workflow = Workflow(definition)
    assert workflow.bindings['firstName'].value == 'dathan'


def test_workflow_records_steps():
    definition = """
bindings:
    firstName: dathan
steps:
    - type: bash
      script: |
        echo "Foo"
    - type: bash
      script: |
        echo "Bar"
"""
    workflow = Workflow(definition)
    data = workflow.run()
    assert len(data['steps']) == 2
    assert data['steps'][0]['output'] == "Foo\n"
    assert data['steps'][0]['status'] == 'SUCCESS'
    assert data['steps'][1]['output'] == "Bar\n"
    assert data['steps'][1]['status'] == 'SUCCESS'

