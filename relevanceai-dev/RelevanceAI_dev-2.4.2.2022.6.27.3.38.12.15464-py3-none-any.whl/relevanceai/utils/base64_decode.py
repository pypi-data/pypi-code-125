"""Base64 decoding for workflows
"""

import base64
import json


def decode_workflow_token(token):
    """It takes a token, decodes it, and returns the decoded token

    Parameters
    ----------
    token
        The token that was generated by the workflow.

    Returns
    -------
        A dictionary of the workflow configuration.

    """
    config = json.loads(base64.b64decode(token + "==="))
    return config
