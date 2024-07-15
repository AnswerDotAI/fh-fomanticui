from fasthtml.common import *
from fh_ui.card import Card
import uvicorn

# Since this is just a CSS POC, for now we don't include jQuery or the js for each CSS framework
stylesheets = {
    'pico': 'https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css',
    'bootstrap': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css',
    # TODO: add daisyui. It also requires tailwindcss separately from https://cdn.tailwindcss.com
    # 'tailwind_daisy': 'https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css',
    'frankenui': 'https://unpkg.com/franken-wc@0.0.2/dist/css/slate.min.css',
    'semanticui': 'https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.css',
}

hdrs = [
    Meta(name='description', content='fh-ui: FastHTML UI'),
    Link(href=stylesheets['semanticui'], rel='stylesheet', id='dynamic-stylesheet'),
    Script(src='https://unpkg.com/htmx.org@2.0.1/dist/htmx.js'),
]

app, rt = fast_app(hdrs=hdrs, live=True, default_hdrs=False)

@rt('/change_stylesheet')
def post(style: str):
    return Link(href=stylesheets[style], rel='stylesheet', id='dynamic-stylesheet')

@rt("/")
def get():
    return (
        Title("fh-ui: FastHTML UI"), 
        Div(
            H1("fh-ui: FastHTML UI", cls='ui header'),
            P("A set of FastHTML components that build upon CSS UI components"),

            A('GitHub fh-ui', href='https://github.com/AnswerDotAI/fh-ui', cls='ui button'),
            Button('PyPI fh-ui', href='pypi.org/project/fh-ui', cls='ui disabled button'),

            H2('Renderer', cls='ui header'),

            Select(
                Option('Pico CSS', value='pico'),
                Option('Bootstrap', value='bootstrap'),
                # Option('Tailwind CSS with DaisyUI', value='tailwind_daisy'),
                Option('Franken UI', value='frankenui'),
                Option('Semantic UI / Fomantic UI', value='semanticui'),
                cls='ui dropdown',
                hx_post='/change_stylesheet',
                hx_trigger='change',
                hx_target='#dynamic-stylesheet',
                hx_swap='outerHTML'
            ),
            
            H2('Cards', cls='ui header'),
            P('The first card is rendered manually. The second card is rendered using the Card class.'),

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
            cls='ui container'
        )
    )

if __name__ == '__main__':
    # TODO: replace with something like run_uv(fname='__main__') 
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=5001)))
