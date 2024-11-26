public class PaymentFactory {
    public static Payment getPayment(String type) {
        if (type.equalsIgnoreCase("CreditCard")) {
            return new CreditCardPayment();
        } else if (type.equalsIgnoreCase("PayPal")) {
            return new PayPalPayment();
        }
        throw new IllegalArgumentException("Invalid payment type: " + type);
    }
}
