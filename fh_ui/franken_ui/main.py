from fasthtml.common import *

from fh_ui.franken_ui import *

hdrs = [
    Meta(name='description', content='FastHTML UI'),
    # Slate is 1 of 12 Franken UI CSS options.
    # TODO: allow easy swapping
    Link(href='https://unpkg.com/franken-wc@0.0.2/dist/css/slate.min.css', rel='stylesheet'),
]

app, rt = fast_app(hdrs=hdrs, live=True, default_hdrs=False)

@rt("/")
def get():
    cards = (Card(
                title="Card Title",
                body=(
                    P("This is a card component."),
                    P("It has a title, body, and footer."),
                ),
                footer="Card Footer",
            ),
            Card(
                title="Card Title",
                body=(
                    P("This is a card component."),
                    P("It has no footer"),
                ),
            ),                     
            Card(
                body=(
                    P("This is a card component."),
                    P("It has no title"),
                ),
                footer="Card Footer",
            ),           
            Card(
                body=(
                    P("This is a card component."),
                    P("It has no title or footer"),
                ),
            ),
    )
    cards = [Div(card) for card in cards]


    return (
        Title("fh-ui: FastHTML UI"), 
        Div(
            H1("fh-ui: FastHTML UI", cls='uk-h1'),
            P("A set of FastHTML components that build upon CSS UI components"),
            A('GitHub fh-ui', href='https://github.com/AnswerDotAI/fh-franken-ui', cls='uk-button uk-button-default'),
            Button('PyPI fh-ui', href='pypi.org/project/fh-ui', cls='uk-button uk-button-default', disabled=True),

            H2('Cards', cls='uk-h2'),
            P('The first card is rendered manually. The second card is rendered using the Card class.'),

            # Div(*cards, cls="uk-child-width-1-2@m uk-grid-small", uk_grid=True),
            
            # Group of cards
            Div(

                # First card is rendered manually
                Div(
                    Div(
                        Img(src='https://via.placeholder.com/150', cls='ui image'),
                        cls='image'
                    ),
                    Div(
                        Div(
                            'Uma the Kid',
                            cls='header'
                        ),
                        Div(
                            'Uma is a girl who swims like a mermaid',
                            cls='description'
                        ),
                        cls='content',
                    ),
                    cls='ui card',
                ),

                # Second card is rendered using the Card class
                Card(
                    title='Hannah the Kid',
                    description='Hannah is a girl who dances and sings',
                    image='https://via.placeholder.com/150',
                    button_links=[('Read More', '#')],
                ),
                cls='ui cards',
            ),
                                                          
            cls='uk-container'
        )
    )

if __name__ == '__main__':
    run_uv()
