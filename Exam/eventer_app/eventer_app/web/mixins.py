from enum import Enum


class ChoicesMixin(Enum):
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class ChoicesLengthMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.name) for x in cls)
