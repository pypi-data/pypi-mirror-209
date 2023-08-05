"""Token plugins can be used to handle specific edge."""


def tokenize(hub, text: str, **kwargs) -> str:
    """Iterate over "token" plugins and handle each unique edge case."""
    for plugin in hub.token._loaded:
        if plugin == "init":
            continue
        hub.log.trace(f"Passing text through tokenizer plugin {plugin}")
        text = hub.token[plugin].tokenize(text, **kwargs)

    return text


def detokenize(hub, text: str) -> str:
    """Iterate over "token" plugins and handle each unique edge case."""
    for plugin in hub.token._loaded:
        if plugin == "init":
            continue
        hub.log.trace(f"Passing text through detokenizer plugin {plugin}")
        text = hub.token[plugin].detokenize(text)

    return text
