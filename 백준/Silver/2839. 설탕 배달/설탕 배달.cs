using System;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int count = 0;

        while (true)
        {
            if (N % 5 == 0)
            {
                count += N / 5;
                Console.WriteLine(count);
                break;
            }
            N -= 3;
            count++;

            if (N < 0)
            {
                Console.WriteLine("-1");
                break;
            }
        }
    }
}