import os
import json
import pytest

from run import create_app

def app():
    app = create_app()
    return app
