import os, subprocess, json
import itertools
import pdb

from workflowregtest import WorkflowRegtest


if __name__ == "__main__":
    Workflow_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),  "workflows4regtests", "basic_examples",)

    for workflow in next(os.walk(Workflow_dir))[1]:
        wf = WorkflowRegtest(os.path.join(Workflow_dir, workflow))
        wf.generate_dockerfiles()
        wf.build_images()
        wf.testing_workflow()
