namespace EX1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Diga um número: ");
            int n = int.Parse(Console.ReadLine());
            Console.Write("Diga outro número: ");
            int m = int.Parse(Console.ReadLine());

            Console.WriteLine($"Soma = {n + m}\nSubtração = {n - m}\nMultiplicação = {n * m}\nDivisão = {n / m}");
        }
    }
}
