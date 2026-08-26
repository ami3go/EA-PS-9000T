class GuiApplicationError(Exception):
    """Base exception for GUI/core wrapper errors."""


class ProfileValidationError(GuiApplicationError):
    """Raised when a CSV voltage profile is invalid."""


class ControllerError(GuiApplicationError):
    """Raised by the controller wrapper for invalid state or backend errors."""


class NotConnectedError(ControllerError):
    """Raised when an operation requires a connected PSU."""
