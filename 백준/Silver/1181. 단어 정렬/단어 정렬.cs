namespace Solution {

    // Linq까  using System.Linq없이 사용가능한지 확인용
    
    class Program {
    static void Main(string[] args) {

      var n = int.Parse(Console.ReadLine()!);

      var words = new string[n];
      for (int i = 0; i < n; i++)
        words[i] = Console.ReadLine()!;

      words = words
            .Distinct()
            .OrderBy(w => w.Length)
            .ThenBy(w => w)
            .ToArray();

      foreach (var word in words)
        Console.WriteLine(word);

    }
  }
}