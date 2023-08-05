"""Creates the structure for the entire project."""


def __virtual__(hub):  # noqa N807
    """Ensure that pop-ml's config options get considered as early as possible."""
    hub.pop.sub.add(dyne_name="config")
    # Ensure that pop_ml's config gets loaded
    hub.config.LOAD.insert(0, "pop_ml")
    return True


def __init__(hub):  # noqa N807
    """Add all of the subs used by pop-ml to the hub."""
    # Perform python imports for the whole project
    hub.pop.sub.add(dyne_name="lib")
    hub.pop.sub.add(python_import="re", sub=hub.lib)
    hub.pop.sub.add(python_import="transformers", sub=hub.lib)
    hub.pop.sub.add(python_import="dict_tools.data", sub=hub.lib, subname="dtd")

    # Add subsystems that are used by pop_ml
    hub.pop.sub.add(dyne_name="token")


def cli(hub):
    """Setup the project for use by CLI."""
    hub.pop.config.load(["pop_ml"], cli="pop_ml")

    hub.pop.loop.create()

    hub.ml.init.run()


def run(hub):
    """This is the entrypoint for the pop-ml cli tool called "pop-translate"."""
    # Initialize the tokenizer from config options
    hub.ml.tokenizer.init(
        model_name=hub.OPT.pop_ml.model_name,
        dest_lang=hub.OPT.pop_ml.dest_lang,
        source_lang=hub.OPT.pop_ml.source_lang,
        pretrained_model=hub.OPT.pop_ml.pretrained_model_class,
        pretrained_tokenizer=hub.OPT.pop_ml.pretrained_tokenizer_class,
    )
    # Split the input text based on newlines
    source = hub.OPT.pop_ml.input_text.split("\n")
    # Translate each line and return the output
    output = hub.ml.tokenizer.translate(source)
    # Print the output
    print("\n".join(output))
