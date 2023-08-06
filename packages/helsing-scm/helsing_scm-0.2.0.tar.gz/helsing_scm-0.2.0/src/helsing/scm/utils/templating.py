import inspect
from textwrap import dedent
from typing import Literal

from mako.template import Template  # type: ignore


def template(template: str, dedent_mode: Literal["dedent"] | None = None, /, **kwargs: object) -> str:
    """
    Render a template string using Mako.

    :param template: The Mako template string.
    :param dedent: Whether to dedent the template string before rendering.
    :param kwargs: The template variables.
    """

    if dedent_mode == "dedent":
        template = dedent(template)
    filename = inspect.stack()[1].filename
    value = Template(template, filename=filename).render(**kwargs)
    assert isinstance(value, str)
    return value
