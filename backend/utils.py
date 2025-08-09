from config import constants

def load_system_settings_template():
    with open(constants.PROMPT_TEMPLATE_PATH, "r") as f:
        prompt_template = f.read()
    return prompt_template




def generate_response(tier_level, files_dict):
    return constants.placeholder_response