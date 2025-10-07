using System;

namespace MyApplication
{
    class Program
    {
        static void Main(string[] args)
        {
            // 1) i want to print numbers with these conditions :
            //    divisble by 3 = print buzz
            //    divisble by 5 = print bizz
            //    divisble by 3 and 5 = print buzzbizz
            for (int i = 1; i <= 100; i++)
            {
                // 3) Make it simpler by using output instead of console writeline
                string output = "";
                if (i % 3 == 0 && i % 5 == 0)
                {
                    output += "buzzbizz";
                }
                else if (i % 3 == 0)
                {
                    output += "buzz";
                }
                else if (i % 5 == 0)
                {
                    output += "bizz";
                }
                // 2) and then divisible by 7 = bazz
                else if (i % 7 == 0)
                {
                    output += "bazz";
                }
                else
                {
                    output += i;
                }
                Console.WriteLine(output);
            }
        }
    }
}
