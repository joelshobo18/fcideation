# Loads API keys from the environment, falling back to ~/.config/lx/.env (never commit keys).
import os
def load():
    p = os.path.expanduser("~/.config/lx/.env")
    if os.path.exists(p):
        for line in open(p):
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1); os.environ.setdefault(k, v)
