"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'detonate_file_1' block
    detonate_file_1(container=container)

    return

@phantom.playbook_block()
def detonate_file_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("detonate_file_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.vaultId","artifact:*.id"])

    parameters = []

    # build parameters list for 'detonate_file_1' call
    for container_artifact_item in container_artifact_data:
        if container_artifact_item[0] is not None:
            parameters.append({
                "limit": 50,
                "comment": "Test file courtesy of Claude",
                "vault_id": container_artifact_item[0],
                "environment": "windows 10, 64-bit",
                "detail_report": True,
                "is_confidential": True,
                "context": {'artifact_id': container_artifact_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("detonate file", parameters=parameters, name="detonate_file_1", assets=["cs"], callback=code_1)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    detonate_file_1_result_data = phantom.collect2(container=container, datapath=["detonate_file_1:action_result.data"], action_results=results)

    detonate_file_1_result_item_0 = [item[0] for item in detonate_file_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'data:  {json.dumps(detonate_file_1_result_item_0, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_block_result(key="code_1__inputs:0:detonate_file_1:action_result.data", value=json.dumps(detonate_file_1_result_item_0))

    phantom.save_block_result(key="code_1_called", value="True")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return