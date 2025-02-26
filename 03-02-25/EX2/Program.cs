namespace EX2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Diga o valor: ");
            int p = int.Parse(Console.ReadLine());
            Console.Write("Diga o desconto: ");
            float d = float.Parse(Console.ReadLine());

            Console.WriteLine(p * (1 - d / 100));
        }
    }
}
