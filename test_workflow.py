import pytest

from workflow import Workflow


def test_initial_bindings():
    definition = """
bindings:
    firstName: dathan
"""
    workflow = Workflow(definition)
    assert workflow.bindings['firstName'].value == 'dathan'


def test_workflow_rejects_non_bash_step():
    definition = """
steps:
    - type: python
      script: |
        print("Foo")
"""
    with pytest.raises(NotImplementedError):
        Workflow(definition)


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


def test_exit_code_64_means_pending():
    definition = """
steps:
    - type: bash
      script: exit 64
"""
    data = Workflow(definition).run()
    assert data['steps'][0]['status'] == 'PENDING'


def test_on_failure_or_pending_do_not_execute_subsequent_steps():
    definition = """
steps:
    - type: bash
      script: exit 64
    - type: bash
      script: echo "This should not get executed"
"""
    data = Workflow(definition).run()
    assert len(data['steps']) == 1
    assert data['steps'][0]['status'] == 'PENDING'


def test_can_pass_variables_between_steps():
    definition = """
bindings:
  firstName: Dathan
steps:
  - type: bash
    script: |
      echo "Hi ${firstName}"
      lastName=Bennett
    input_variables: [firstName]
    output_variables: [lastName]
  - type: bash
    script: |
      echo "Hi ${firstName} ${lastName}"
    input_variables: [firstName, lastName]
"""
    data = Workflow(definition).run()
    assert data['steps'][1]['output'] == "Hi Dathan Bennett\n"
