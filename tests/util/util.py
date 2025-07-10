from fplpy.objects._element.model import Model


def wrap_argument(model: Model) -> dict[str, Model]:
    return {"attributes": model}
