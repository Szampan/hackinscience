import textwrap
import itertools

def sidebyside(left, right, width=79):
    half = int(width / 2 - 1)    
    if width % 2 != 0:
        half = int((width-1) / 2)    

    LEFT = textwrap.wrap(left, half)
    RIGHT = textwrap.wrap(right, half)
    result = ""
    ZIP = list(itertools.zip_longest(LEFT, RIGHT, fillvalue = ""))

    for i in ZIP:
        if result != "":
            result += "\n"
        result += (f"{str(i[0]):<{half}}|{str(i[1]):<{half}}")

    return result




# Test your code with those values if you want (but don't submit your tests)
left = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed non risus. "
    "Suspendisse lectus tortor, dignissim sit amet, "
    "adipiscing nec, utilisez sed sin dolor."
)

right = (
    "Morbi venenatis, felis nec pretium euismod, "
    "est mauris finibus risus, consectetur laoreet "
    "sem enim sed arcu. Maecenas sit amet eleifend sem. "
    "Nullam ac libero metus. Praesent ac finibus nulla, vitae molestie dolor."
    " Aliquam vestibulum viverra nisl, id porta mi viverra hendrerit."
    " Ut et porta augue, et convallis ante."
)

if __name__ == "__main__":
    print(sidebyside(left, right, 50))