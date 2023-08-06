"""
GPT class file.
"""
import openai
from enum import Enum
from typing import Any


def config(key: str, organization: str = None) -> None:
    """
    Provide a valid OpenAI Api Key to provide to the openai package
    """
    openai.api_key = key
    if organization is not None:
        openai.organization = organization


def compile_messages(messages: list[list[str, str | str, None]], system: str = None, ) -> list[dict]:
    """
    Compile a list of message dictionaries given a list of lists [user_prompt, gpt_response], and an optional system message.    
    """
    formatted_messages = messages.copy()
    formatted_messages = [] if not system else [{"role": "system", "content": system}]
    for exchange in messages:
        formatted_messages.append({"role": "user", "content": exchange[0]})
        if exchange[1] is not None:
            formatted_messages.append({"role": "assistant", "content": exchange[1]})
    return formatted_messages


class Model(Enum):
    """
    This Enum class represents the available GPT models that can be used.

    Each model is represented by a tuple that contains the model's identifier string 
    and two rate values. The first rate value corresponds to the cost per 1000 tokens 
    for prompts, and the second rate value corresponds to the cost per 1000 tokens 
    for completions.

    Available models:
        GPT4: Represents the GPT-4 model with identifier "gpt-4"
        GPT4_32K: Represents the GPT-4 model with 32k token support, identifier "gpt-4-32k"
        GPT3_5: Represents the GPT-3.5 model with identifier "gpt-3.5-turbo"
    """
    GPT4 = ("gpt-4", 0.03, 0.06)
    GPT4_32K = ("gpt-4-32k", 0.06, 0.12)
    GPT3_5 = ("gpt-3.5-turbo", 0.002, 0.002)


class GPT():
    """
    A class that can create and manage a single context-driven instance of a GPT model.
    """
    _model: str
    _system: str
    _cost: float
    messages: list[list]
    cost: str
    prompt_tokens: int
    completion_tokens: int

    def __init__(self, model: Model = Model.GPT3_5, system: str = None) -> None:
        """
        Initiates an instance of a GPT model. Provide the GPT model you would like to use by accessing the <gpt.Model> enum and optionally provide a system prompt.
        """
        self.change_model(model)
        self._system = system
        self._cost = 0.0 
        self.messages = []
        self.cost = str
        self.prompt_tokens = 0
        self.completion_tokens = 0

    def response(self, prompt: str, just_reply=True, **kwargs: Any) -> str | dict:
        """
        Obtain a context-driven response from GPT given the specified prompt.
        """
        self.messages.append([prompt, None])
        messages = compile_messages(self.messages, self._system)
        response = openai.ChatCompletion.create(
            model=self._model,
            messages=messages,
            **kwargs,
        )
        if response is None:
            raise Exception(
                "The ChatCompletions request was not successfully made.")
        p = response["usage"]["prompt_tokens"]
        c = response["usage"]["completion_tokens"]
        self.prompt_tokens += p
        self.completion_tokens += c
        self._cost += (p / 1000) * \
            self._rate[0] + (c / 1000) * self._rate[1]
        self.cost = f"${self._cost:.2f}"
        reply = response["choices"][0]["message"]["content"]
        self.messages[-1][1] = reply

        return reply if just_reply else response

    def change_model(self, model: Model) -> None:
        """
        Changes the model given a <gpt.Model> argument.
        """
        if not isinstance(model, Model):
            raise ValueError(
                "Provide a valid model using the <gpt.Model> datatype.")

        self._model = model.value[0]
        self._rate = tuple(model.value[1:])

    def get_messages(self) -> list[dict[str]]:
        """
        Returns the message history as a list of message dictionaries.
        """
        messages = []
        for exchange in self.messages:
            user_message, gpt_message = {
                "user": exchange[0]}, {"assistant": exchange[1]}
            messages.extend([user_message, gpt_message])

        return messages