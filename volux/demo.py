class VoluxDemo:
    def __init__(self, demo_name, demo_method, alias, requirements=None, *args, **kwargs):
        self._name = demo_name
        self._method = demo_method
        self._alias = alias
        self._requirements = requirements # optional

    def run(self):
        self._method()

    # def __str__(self):
    #     header = "[DEMO:{name}]----".format(name=self._alias)
    #     divider = "-"*len(header)
    #     body = "Name: {name}\nAlias: {alias}\nRequirements: {requirements}".format(name=self._name,requirements=self._requirements, alias=self._alias)
    #
    #     return("{header}\n{body}\n{divider}".format(header=header,divider=divider,body=body))

    def __repr__(self):
        return "<VoluxDemo '{}'>".format(self._alias)
