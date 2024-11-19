from booking_strategy import BookingStrategy  # Import the abstract base class
import re

class FlightBooking:
    """
    Concrete strategy implementation for flight booking.
    """
    # List of available flights
    available_flights = ["Flight123", "AirIndia101", "Delta456", "United789"]

    def book(self, details):
        """
        Books a flight after validating input details.
        :raises ValueError: If validation fails
        :return: Confirmation message
        """
        # Extract details
        flight = details.get("flight")
        date = details.get("date")

        # Validate flight name and date
        if not flight or not date:
            raise ValueError("Flight name and date cannot be empty or None.")

        if not re.match(r"^[a-zA-Z0-9\s]+$", flight):
            raise ValueError("Flight name contains invalid characters.")

        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            raise ValueError("Date must be in the format YYYY-MM-DD.")

        # Check if flight is available
        if flight not in self.available_flights:
            raise ValueError(f"Flight '{flight}' is not available. Please select a valid flight.")

        # Proceed with booking if validation passes
        print(f"Flight booked: {flight} on {date}")
        return f"Booking confirmed for flight: {flight} on {date}"