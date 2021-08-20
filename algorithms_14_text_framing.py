from dataclasses import dataclass, replace
from datetime import datetime

@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"

fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


def frame_text(text: str, frame: Frame) -> str:
    LINES = text.splitlines()
    width = len(max(LINES, key = len))
    
    def side_frames(input, w):  # zamiast tej funkcji można dać coś w stylu mid = f"{frame.left}{i:<{w}}{frame.right}\n" for i in LINES
        out = ""
        for i in input:
            out += f"{frame.left}{i:<{w}}{frame.right}\n"
        return out
    

    top = frame.top_left + frame.top *width + frame.top_right + "\n"
    mid = side_frames(LINES, width)      #### JAK ODCZYTAĆ DŁUGOŚĆ NAJDŁUŻSZEGO WIERSZA W KILKUWIERSZOWYM STRINGU?? -> text.splitlines()
    bottom = frame.bottom_left + frame.bottom *width + frame.bottom_right + "\n"
    
    content = top + mid + bottom
    
    return content

# print(frame_text(f"It is {datetime.now():%H:%I:%S}.", fancy_frame))

text = """It is 16h19.
And it's raining."""
text = frame_text(text, fancy_frame)
text = frame_text(text, fancy_frame)
print(frame_text(text, fancy_frame))

