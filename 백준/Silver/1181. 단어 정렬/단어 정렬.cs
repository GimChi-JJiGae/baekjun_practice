using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        HashSet<string> wordSet = new HashSet<string>();

        for (int i = 0; i < n; i++)
        {
            string word = Console.ReadLine();
            wordSet.Add(word);
        }

        List<string> wordList = wordSet.ToList();

        wordList.Sort((a, b) =>
        {
            if (a.Length == b.Length)
            {
                return string.Compare(a, b);
            }
            return a.Length.CompareTo(b.Length);
        });

        foreach (string word in wordList)
        {
            Console.WriteLine(word);
        }
    }
}
