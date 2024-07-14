from fasthtml import xt

__all__ = ["Card"]


def Card(*content, title: str, paragraph: str) -> str:
    return xt.Div(
        xt.H3(title, cls="uk-card-title"),
        xt.P(paragraph, cls="uk-margin"),
        cls="uk-width-1-2@m uk-card uk-card-body uk-card-default",
    )
