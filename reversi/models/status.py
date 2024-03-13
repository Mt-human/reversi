from enum import Enum

class Status(Enum):
    SPACE = {
    "label": "space",
    "value": "・"
    }

    BLACK = {
    "label": "black",
    "value": "●"
    }   

    WHITE = {
    "label": "white",
    "value": "○"
    }

    @staticmethod
    def label_of(l: str):
        for k in Status:
            if Status.label == l:
                return Status.value
        raise ValueError(f"undefined Status: {l}")