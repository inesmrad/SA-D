from flight_booking import FlightBooking
from hotel_booking import HotelBooking
from booking_context import BookingContext

if __name__ == "__main__":
    """
    Entry point for the booking system.
    Allows users to choose a booking type (flight or hotel) and provides relevant inputs.
    """
    print("Welcome to the Travel Booking System!")
    print("Choose booking type: flight or hotel")
    booking_type = input("Enter booking type: ").strip().lower()
    context = None

    try:
        # Determine booking type and collect details
        if booking_type == "flight":
            context = BookingContext(FlightBooking())
            details = {
                "flight": input("Enter flight name: ").strip(),
                "date": input("Enter travel date (YYYY-MM-DD): ").strip()
            }
        elif booking_type == "hotel":
            context = BookingContext(HotelBooking())
            details = {
                "hotel": input("Enter hotel name: ").strip(),
                "nights": int(input("Enter number of nights: ").strip())
            }
        else:
            raise ValueError("Invalid booking type. Please choose 'flight' or 'hotel'.")

        # Execute booking and print confirmation
        confirmation = context.execute_booking(details)
        print(confirmation)
    except ValueError as e:
        # Handle validation errors
        print(f"Error: {e}")
