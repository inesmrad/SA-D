import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double balance = 500.00;

        System.out.print("Enter payment type (CreditCard, PayPal): ");
        String paymentType = scanner.nextLine();

        System.out.print("Enter amount to be paid: ");
        double amount = scanner.nextDouble();

        if (amount > balance) {
            System.out.println("Insufficient balance. Payment cannot be processed.");
        } else {
            try {
                Payment payment = PaymentFactory.getPayment(paymentType);
                payment.processPayment(amount);

                balance -= amount;
                System.out.println("Payment successful! Remaining balance: $" + balance);
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }

        scanner.close();
    }
}

