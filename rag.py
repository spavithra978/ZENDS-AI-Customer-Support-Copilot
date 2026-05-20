from policy_data import policy_dict

def retrieve_policy(intent):

    return policy_dict.get(
        intent,
        "This query is not covered under current ZENDS policies."
    )