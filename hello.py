"""Minimal entry point for the codebuddy-demo repository."""


def greet(name: str = "CodeBuddy") -> str:
    """Return a greeting for the given name."""
    return f"Hello from {name}."


if __name__ == "__main__":
    print(greet())
