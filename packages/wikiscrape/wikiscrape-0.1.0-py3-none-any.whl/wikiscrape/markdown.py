class Markdown:
    @staticmethod
    def a(page, alias=None):
        return f"[[{page}|{alias}]]" if alias else f"[[{page}]]"

    @staticmethod
    def b(text):
        return f"'''{text}'''"

    @staticmethod
    def em(text):
        return f"''{text}''"

    @staticmethod
    def h(level, text):
        return f"{'=' * (level+1)}{text}{'=' * (level+1)}"

    @staticmethod
    def ul(items):
        return "\n".join([f"* {item}" for item in items])

    @staticmethod
    def br():
        return "<br/>"

    @staticmethod
    def hr():
        return "\n----\n"

    @staticmethod
    def comment(text):
        return f"<!-- {text} -->"

    @staticmethod
    def template(content):
        return f"{'{{'}{content}{'}}'}"
