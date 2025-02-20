"""Shared auth layout."""
import pynecone as pc

from ..components import container


def auth_layout(*args):
    """The shared layout for the login and sign up pages."""
    return pc.box(
        container(
            pc.heading(
                pc.span("Welcome to PySocial!"),
                pc.span("Sign in or sign up to get started."),
                display="flex",
                flex_direction="column",
                align_items="center",
                text_align="center",
            ),
            pc.text(
                "See the source code for this demo app ",
                pc.link(
                    "here",
                    href="https://github.com/pynecone-io/pynecone-examples",
                    color="blue.500",
                ),
                ".",
                color="gray.500",
                font_weight="medium",
            ),
            *args,
            border_top_radius="lg",
            box_shadow="0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
            display="flex",
            flex_direction="column",
            align_items="center",
            py=12,
            gap=4,
        ),
        h="100vh",
        pt=16,
        background="url(bg.svg)",
        background_repeat="no-repeat",
        background_size="cover",
    )
