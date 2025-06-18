using System;

class Program
{
    static void Main()
    {
        string[] input = Console.ReadLine().Split();
        int[] sticks = Array.ConvertAll(input, int.Parse);


        Array.Sort(sticks);
        Array.Reverse(sticks);

        int a = sticks[0];
        int b = sticks[1];
        int c = sticks[2];


        if (b + c <= a)
        {
            a = b + c - 1;
        }

        int perimeter = a + b + c;
        Console.WriteLine(perimeter);
    }
}