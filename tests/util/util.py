from fplpy.unlinked_object._element.model import Model


def wrap_argument(model: Model) -> dict[str, Model]:
    return {"attributes": model}
