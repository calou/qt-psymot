class StimuliValue():
    def __init__(self, sql_id=-1, name="", value="", content=""):
        self.id = sql_id
        self.name = name
        if not value:
            self.value = name
        else:
            self.value = value
        self.content = content