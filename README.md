# fh-ui

FastHTML UI components that can be rendered with the structure of your preferred CSS UI framework

Still building out this POC, still unstable.

As a POC, we have a FastHTML `Card` that can be rendered with any of:

* [Pico CSS](https://picocss.com/docs/card)
* [Bootstrap](https://getbootstrap.com/docs/5.3/components/card/)
* [Tailwind with Daisy UI](https://daisyui.com/components/card/)
* [Franken UI](https://franken-ui.dev/docs/card)
* [Semantic UI / Fomantic UI](https://fomantic-ui.com/views/card.html)

## Quickstart

Run main.py:

```bash
python fh_ui/main.py
```

Open it in the browser. You'll see 2 cards:

* A card rendered from XT components to match https://fomantic-ui.com/views/card.html
* A card rendered from a generic Card dataclass using `render_semanticui()`

The renderer dropdown doesn't work yet, but so far for the Semantic UI renderer you can:

* Compare the code for both cards in main.py and card.py
* Notice how there is a renderer registry with the ability to register new renderers
* See what other renderers could look like
* Look at how new renderers would work
* Imagine people creating third-party packages with new renderers
