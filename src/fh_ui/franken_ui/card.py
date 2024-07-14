from typing import Sequence, Any

from fasthtml import xt

__all__ = [
    "Card",
]


def Card(
    title: Sequence[Any] | str | None = None,
    body: Sequence[Any] | None = None,
    footer: Sequence[Any] | str | None = None,
    w_numerator: int = 1,
    w_denominator: int = 4,
) -> list:
    if isinstance(title, str): 
        title = [title]
    if isinstance(footer, str): 
        footer = [footer]        
    return xt.Div(
        xt.Div(xt.H3(*title, cls="uk-card-title"), cls="uk-card-header") if title else xt.Span(),
        xt.Div(*body, cls="uk-card-body") if body else xt.Span(),
        xt.Div(*footer, cls="uk-card-footer") if footer else xt.Span(),
        cls=f"uk-card uk-card-body uk-card-default uk-width-{w_numerator}-{w_denominator}@m"
    )
