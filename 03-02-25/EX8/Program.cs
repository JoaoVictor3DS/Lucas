namespace EX8
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Diga um numero: ");
            int n = int.Parse(Console.ReadLine());

            for (int i = 2; i < n/2; i++)
            {
                if (n % i == 0)
                {
                    Console.WriteLine("Nao e primo");
                    return;
                }
            }

            Console.WriteLine("E primo");
        }
    }
}
