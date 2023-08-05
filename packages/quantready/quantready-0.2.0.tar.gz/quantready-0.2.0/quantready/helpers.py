from collections.abc import Iterable


def _snakecase(text: str) -> Iterable[str]:
    if (text is None) or len(text.strip()) <= 1:
        yield text
        return
    text = text.strip()
    for i, c in enumerate(text[:-1]):
        c = c.replace(" ", "_")
        yield c
        if c in "_" or text[i + 1] == "_":
            pass
        elif text[i + 1].isupper() and not c.isupper():
            yield "_"
        elif c.isdigit() and not text[i + 1].isdigit():
            yield "_"
    yield text[-1].replace(" ", "_")


def snakecase(text: str | None) -> str | None:
    return None if text is None else "".join(_snakecase(text)).lower()
