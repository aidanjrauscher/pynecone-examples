"""A container component."""
import pynecone as pc


def container(*children, **props):
    """A fixed container based on a 960px grid."""
    # Enable override of default props.
    props = (
        dict(
            width="100%",
            max_width="960px",
            bg="white",
            h="100%",
            px=[4, 12],
            margin="0 auto",
            position="relative",
        )
        | props
    )
    return pc.box(*children, **props)
