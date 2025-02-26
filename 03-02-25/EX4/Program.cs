namespace EX4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Diga o Primeiro Numero: ");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Diga o Segundo Numero: ");
            int b = int.Parse(Console.ReadLine());

            int soma = 0;
            for (int i = a; i <= b; i++)
            {
                soma += i;
            }
            Console.WriteLine("Soma = " + soma);
        }
    }
}
