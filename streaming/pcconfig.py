import pynecone as pc

class StreamingConfig(pc.Config):
    pass

config = StreamingConfig(
    app_name="streaming",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)