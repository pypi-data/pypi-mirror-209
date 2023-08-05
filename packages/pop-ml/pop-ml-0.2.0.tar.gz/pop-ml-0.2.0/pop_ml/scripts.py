#!/usr/bin/env python3
"""Entry point of the project for use by setup.py for the CLI-based command(s)."""
import pop.hub


def start():
    """Initialize the hub and make the primary project available on the hub."""
    # Initialize the hub
    hub = pop.hub.Hub()
    # Initialize the namespace on the hub
    hub.pop.sub.add(dyne_name="ml")
    # Call the CLI function
    hub.ml.init.cli()
