class Pig:
    """
    猪只类
    """

    treat: dict[str, str]

    def __init__(self, ear_tag: str, **kwargs):
        self.ear_tag = ear_tag
        self.treat = {}
        self.attributes = kwargs

    def __repr__(self) -> str:
        return f"猪只编号{self.ear_tag},"

    def __getattr__(self, name):
        try:
            return self.attributes[name]
        except KeyError:
            raise AttributeError(f"'Pig' object has no attribute '{name}'")

    def update(self, ear_tag: str, **kwargs):
        self.ear_tag = ear_tag
        self.attributes = kwargs

    def treating(self, date: str, medicine: str):
        """
        给猪喂药
        :param date:
        :param medicine:
        """
        self.treat.setdefault(date, medicine)

    def get_treat(self, date):
        """
        获取猪的喂药记录
        :param date:
        :return:
        """
        return self.treat[date] if date in self.treat else None
