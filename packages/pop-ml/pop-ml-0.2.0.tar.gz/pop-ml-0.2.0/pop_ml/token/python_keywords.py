"""Plugin to handle tokenizing and detokenizing python keywords."""

import re

PLACEHOLDER = "KW_{keyword}"

# Always avoid translating these keywords
ALWAYS_KEYWORDS = [
    # It's rare that these words would be capitalized in any context and need to be translated
    "False",
    "None",
    "Python",
    "True",
    # These are not english dictionary words and are specific to python
    "async",
    "await",
    "def",
    "del",
    "elif",
    "nonlocal",
]
# Create the regex pattern for the keywords always transformed
ALWAYS_PATTERN = r"\b(?:{})\b".format("|".join(map(re.escape, ALWAYS_KEYWORDS)))

# Avoid translating these keywords if they show up at the beginning of a line
BEGINNING_KEYWORDS = [
    "assert",
    "break",
    "class",
    "continue",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "import",
    "lambda",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]

BEGINNING_PATTERN = r"(?m)^(?:{})".format(
    "|".join(
        map(
            re.escape,
            BEGINNING_KEYWORDS,
        )
    )
)


def tokenize(hub, text: str, **kwargs) -> str:
    """Transform python keywords into tokens that are ignored by the tokenizer."""
    # Replace keywords that are always transformed
    replaced_text = hub.lib.re.sub(
        ALWAYS_PATTERN, lambda match: PLACEHOLDER.format(keyword=match.group()), text
    )

    # Replace keywords at the beginning of a line
    replaced_text = hub.lib.re.sub(
        BEGINNING_PATTERN,
        lambda match: PLACEHOLDER.format(keyword=match.group()),
        replaced_text,
    )

    return replaced_text


def detokenize(hub, text: str) -> str:
    """Transform the tokens back into their original strings."""
    return hub.lib.re.sub(r"\bKW_(\w+)\b", r"\1", text)
