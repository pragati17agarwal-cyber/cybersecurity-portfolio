// A q a 1 z Q !
#include <stdio.h>

int main(void)
{
    long long number;

    printf("Number: ");
    scanf("%lld", &number);

    // keep a copy of the original number, since we'll destroy `number` below
    long long original = number;

    // Step 1: Luhn's algorithm to check validity, and count digits
    int sum = 0;
    int digit_count = 0;
    int position = 0;   // 0 = rightmost digit, 1 = next, etc.

    while (number > 0)
    {
        int digit = number % 10;

        if (position % 2 == 1)   // every second digit, counting from the right
        {
            digit *= 2;
            if (digit > 9)
            {
                digit -= 9;   // same as adding its two digits together
            }
        }

        sum += digit;
        number /= 10;
        position++;
        digit_count++;
    }

    int valid = (sum % 10 == 0);

    // Step 2: get the first two digits of the original number
    long long temp = original;
    while (temp >= 100)
    {
        temp /= 10;
    }
    int first_two = temp;        // e.g. 40 for 4003..., 37 for 3782...
    int first_one = first_two / 10;

    // Step 3: classify, only if Luhn check passed
    if (valid && digit_count == 15 && (first_two == 34 || first_two == 37))
    {
        printf("AMEX\n");
    }
    else if (valid && digit_count == 16 && first_two >= 51 && first_two <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if (valid && (digit_count == 13 || digit_count == 16) && first_one == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}