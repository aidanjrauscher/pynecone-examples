"""A Pynecone app demonstrating streaming with ChatGPT."""

import pynecone as pc
import asyncio
import openai

from .styles import style

class State(pc.State):
    text = ""
    prompt= ""
    _OPENAI_API_KEY= "YOUR OPENAI API KEY HERE..."

    async def generate_response(self):
        # generate openai response
        self.set_text("")
        openai.api_key = self._OPENAI_API_KEY
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[ {"role": "user", "content": self.prompt} ],
                temperature=0,
                max_tokens=500,
                stream=True
            )
            # stream chunk content
            for chunk in response:
                content = chunk["choices"][0].get("delta", {}).get("content")
                if content is not None:
                    self.text += content
                await asyncio.sleep(0.11)
                yield

        except Exception as e:
            return
        
    @pc.var
    def is_prompt_empty(self)->bool:
        return not self.prompt
    
def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Stream ChatGPT", size="2xl"),
            pc.flex(
                pc.input(
                    placeholder="Send a message to ChatGPT...",
                    value=State.prompt,
                    on_change=State.set_prompt,
                    width="90%",
                    height="50%",
                    font_weight="semibold",
                    _placeholder="{{color: '$4e4e5d'}}"
                ),
                pc.button(
                    "Enter",
                    on_click=State.generate_response,
                    is_disabled=State.is_prompt_empty,
                    height="50%",
                    font_weight="bold",
                    font_size="0.65em",
                    background_color="#19C37D"
                ),
                justify="center",
                align="center",
                gap="0.4em",
                height="3em",
                width="70vw",
                rounded="md",
                wrap="wrap"
            ),
            pc.heading(
                    "Response", 
                    size="xl",
            ),
            pc.divider(
                border_width="2px",
                width="60vw"
            ),
            pc.box(
                pc.markdown(
                    State.text
                ),
                width="60vw",
                padding="5px",
            ),
            spacing="2em",
            font_size="2em",
        ),
        padding="2%"
    )


# Add state and page to the app.
app = pc.App(state=State, style=style)
app.add_page(index)
app.compile()
