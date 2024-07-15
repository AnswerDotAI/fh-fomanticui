from calendar import c
from dataclasses import dataclass
from typing import List, Tuple, Optional, Callable, Dict
from fasthtml.common import *

# Global registry for renderers
renderer_registry: Dict[str, Callable] = {}

def register_renderer(framework: str):
    """Decorator to register a renderer for a specific framework."""
    def decorator(func: Callable):
        renderer_registry[framework] = func
        return func
    return decorator

@dataclass
class Card:
    title: str; description: str; image: Optional[str] = None; button_links: List[Tuple[str, str]] = ()
    def __xt__(self, uiframework='semanticui'):
        if uiframework not in renderer_registry:
            raise ValueError(f"No renderer registered for framework: {uiframework}")
        return renderer_registry[uiframework](self)

# Default renderers
# TODO: move to separate files once the architecture stabilizes
@register_renderer('semanticui')
def render_semanticui(card: Card):
    card_elements = []

    # Add image div if there's an image
    if card.image:
        card_elements.append(Div(Img(src=card.image, cls='ui image'), cls='image'))

    # Create content div
    content = [
        A(card.title, cls='header'),
        Div(card.description, cls='description')
    ]
    card_elements.append(Div(*content, cls='content'))

    # Add buttons in extra content div if there are any
    if card.button_links:
        buttons = [
            A(text, href=link, cls='ui button')
            for text, link in card.button_links
        ]
        card_elements.append(Div(*buttons, cls='extra content'))

    # Return the complete card
    return Div(*card_elements, cls='ui card')

@register_renderer('frankenui')
def render_frankenui(card: Card):
    return Div(
        H3(card.title, cls='card-title'),
        P(card.description, cls='uk-margin'),
        A("Add Friend", href="#"),
        A("View Profile", href="#"),
        cls='uk-card uk-card-default uk-card-body'
    )

@register_renderer('bootstrap')
def render_bootstrap(card: Card):
    img = Img(src=card.image, cls='card-img-top') if card.image else ''
    buttons = [
        A(text, href=link, cls='btn btn-primary')
        for text, link in card.button_links
    ]

    return Div(
        img,
        Div(
            H5(card.title, cls='card-title'),
            P(card.description, cls='card-text'),
            *buttons,
            cls='card-body'
        ),
        cls='card'
    )

# Usage remains the same
cards_data = [
    Card("Elliot Fu", "Elliot Fu is a film-maker from New York.", image="elliot.jpg", button_links=[("Add Friend", "#")]),
    Card("Veronika Ossi", "Veronika Ossi is a set designer living in New York who enjoys kittens, music, and partying.", image="veronika.jpg", button_links=[("Add Friend", "#"), ("View Profile", "#")]),
    Card("Jenny Hess", "Jenny is a student studying Media Management at the New School", button_links=[("Add Friend", "#")])
]

semantic_cards = [card.__xt__('semanticui') for card in cards_data]
bootstrap_cards = [card.__xt__('bootstrap') for card in cards_data]

semantic_result = Div(*semantic_cards, cls='ui cards')
bootstrap_result = Div(*bootstrap_cards, cls='card-deck')


if __name__ == '__main__':
    print(semantic_result)
    print(bootstrap_result)