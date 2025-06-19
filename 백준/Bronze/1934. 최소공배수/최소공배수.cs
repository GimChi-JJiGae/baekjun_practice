using System;

class sol{
    static void Main(){
        int n = int.Parse(Console.ReadLine());
        for(int i=0; i < n; i++){
            string[] input = Console.ReadLine().Split();
            int a = int.Parse(input[0]);
            int b = int.Parse(input[1]);
      
            Console.WriteLine((a * b) / gcd(a, b));
        }
    }

    static int gcd(int a, int b){
        return (a % b == 0 ? b: gcd(b, a % b));
    }
}