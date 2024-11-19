from booking_strategy import BookingStrategy  # Import the abstract base class
import re

class BookingContext:
    """
    Context class to manage and execute booking strategies.
    """
    def __init__(self, strategy: BookingStrategy):
        """
        Initializes the context with a booking strategy.
        """
        self.strategy = strategy

    def set_strategy(self, strategy: BookingStrategy):
        """
        Dynamically sets the booking strategy.
       updates the booking strategy
        """
        self.strategy = strategy

    def execute_booking(self, details):
        """
        Executes the booking process using the current strategy.
        
        """
        return self.strategy.book(details)
