"""POP project configuration data.

``conf.py`` defines:

* How the CLI args are presented
* All configuration defaults
* Help documentation
* And more

Resources:

* `Intro to pop-config`<https://pop-config.readthedocs.io/en/latest/topics/introduction.html>__
"""

CONFIG = {
    "config": {
        "default": None,
        "help": "Load extra options from a configuration file onto hub.OPT.ml",
    },
    "source_lang": {
        "default": "en",
        "help": "The two-letter code for the source language, this helps automatically select a pretrained model",
    },
    "dest_lang": {
        "default": None,
        "help": "The two-letter code for the target language, this helps automatically select a pretrained model",
    },
    "model_name": {
        "default": None,
        "help": "The specific model to use.  This option ignores source_lang and dest_lang",
    },
    "pretrained_model_class": {
        "default": "MarianMTModel",
        "help": "The pretrained transformer model class to use",
    },
    "pretrained_tokenizer_class": {
        "default": "MarianTokenizer",
        "help": "The pretrained transformer tokenizer class to use",
    },
}

SUBCOMMANDS = {}

CLI_CONFIG = {
    "config": {"options": ["-c"]},
    "source_lang": {"options": ["--translate-from"]},
    "dest_lang": {"options": ["--translate-to"]},
    "model_name": {},
    "input_text": {"positional": True},
}

DYNE = {"ml": ["ml"], "token": ["token"]}
