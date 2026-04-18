# template_selector.py

def choose_template(prompt: str):
    p = prompt.lower()

    if "startup" in p or "pitch" in p:
        return "templates/startup.pptx"
    elif "business" in p:
        return "templates/business.pptx"
    elif "education" in p or "training" in p:
        return "templates/education.pptx"

    return None  # default blank ppt