namespace EX6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] n = new int[5];
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Diga o numero " + (i + 1) + ": ");
                n[i] = int.Parse(Console.ReadLine());
            }

            Console.WriteLine("Diga o numero para procurar: ");
            int opt = int.Parse(Console.ReadLine());

            for (int i = 0; i < 5; i++)
            {
                if (n[i] == opt)
                {
                    Console.WriteLine("Numero presente");
                    return;
                }
            }
        }
    }
}
