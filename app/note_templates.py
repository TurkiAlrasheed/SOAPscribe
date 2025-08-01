def generate_soap_note(info):
    return f"""
S: {info['subjective']}

O: {info['objective']}

A: {info['assessment']}

P: {info['plan']}
""".strip()