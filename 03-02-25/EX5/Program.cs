namespace EX5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] n = new int[5];
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Diga o numeoro " + (i+1) + ": ");
                n[i] = int.Parse(Console.ReadLine());
            }
            for (int i = 4; i >= 0; i--)
            {
                Console.WriteLine("Numero: " + n[i]);
            }
        }
    }
}
