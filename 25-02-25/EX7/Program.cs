namespace EX7
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var notas = new List<float>();

            for (int i = 0; i < 3; i++)
            {
                Console.Write("Nota " + (i + 1) + ": ");
                notas.Add(float.Parse(Console.ReadLine()));
            }

            float soma = notas.Sum();

            Console.WriteLine($"Media: {soma / 3}");
        }
    }
}
