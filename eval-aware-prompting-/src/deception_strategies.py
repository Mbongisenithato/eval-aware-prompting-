def evaluation_aware_rewrite(prompt):
    if "shrink" in prompt:
        return prompt.replace("shrink", "adjust fit")
    return prompt

def add_contextual_softeners(prompt):
    return f"Just curious — {prompt}"