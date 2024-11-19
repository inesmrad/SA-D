from booking_strategy import BookingStrategy  # Import the abstract base class
import re

class HotelBooking:
    """
    Concrete strategy implementation for hotel booking.
    """

    # List of available hotels
    available_hotels = ["GrandHotel", "SeaViewResort", "MountainInn", "CityLodge"]

    def book(self, details):
        """
        Books a hotel after validating input details.
        
        :raises ValueError: If validation fails
        :return: Confirmation message
        """
        # Extract details
        hotel = details.get("hotel")
        nights = details.get("nights")

        # Validate hotel name and number of nights
        if not hotel or nights is None:
            raise ValueError("Hotel name and nights cannot be empty or None.")

        if not re.match(r"^[a-zA-Z0-9\s]+$", hotel):
            raise ValueError("Hotel name contains invalid characters.")

        if hotel not in self.available_hotels:
            raise ValueError(f"Hotel '{hotel}' is not available. Please select a valid hotel.")

        if not isinstance(nights, int) or nights <= 0:
            raise ValueError("Number of nights must be a positive integer.")

        # Proceed with booking if validation passes
        print(f"Hotel booked: {hotel} for {nights} nights")
        return f"Booking confirmed for hotel: {hotel} for {nights} nights"
