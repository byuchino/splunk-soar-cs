"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'list_groups_1' block
    list_groups_1(container=container)

    return

@phantom.playbook_block()
def list_groups_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("list_groups_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "limit": 50,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("list groups", parameters=parameters, name="list_groups_1", assets=["cs"], callback=code_1)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    list_groups_1_result_data = phantom.collect2(container=container, datapath=["list_groups_1:action_result.data"], action_results=results)

    list_groups_1_result_item_0 = [item[0] for item in list_groups_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'data:  {json.dumps(list_groups_1_result_item_0, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_block_result(key="code_1__inputs:0:list_groups_1:action_result.data", value=json.dumps(list_groups_1_result_item_0))

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