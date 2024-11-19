from abc import ABC, abstractmethod

class BookingStrategy(ABC):
    """
    Abstract base class for booking strategies.
    Defines the `book` method that all strategies must implement.
    """
    @abstractmethod
    def book(self, details):
        """
        Abstract method to handle booking.
       to be implemented by concrete strategies.
        """
        pass
