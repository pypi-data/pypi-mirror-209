"""Contracts that define what a token plugin requires."""


def sig_tokenize(hub, text: str, **kwargs) -> str:
    """Contract to enforce that a tokenize function exists in files under the token subsystem."""
    return text


def sig_detokenize(hub, text: str) -> str:
    """Contract to enforce that a detokenize function exists in files under the token subsystem."""
    return text
