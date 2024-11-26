using System;
using System.Collections.Generic;

namespace AplusB
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split();
            Console.WriteLine(int.Parse(input[0]) + int.Parse(input[1]));
        }
    }
}