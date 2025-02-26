namespace EX10
{
    internal class Calculadora
    {
        public static int Soma(int[] n)
        {
            return n[0] + n[1];
        }
        public static int Subtracao(int[] n)
        {
            return n[0] - n[1];
        }
        public static int Multiplicacao(int[] n)
        {
            return n[0] * n[1];
        }
        public static int Divisao(int[] n)
        {
            return n[0] / n[1];
        }

    }
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] n = new int[2];

            Console.WriteLine("Diga o primeiro numero");
            n[0] = int.Parse(Console.ReadLine());
            Console.WriteLine("Diga o segundo numero");
            n[1] = int.Parse(Console.ReadLine());

            Console.WriteLine("Soma: " + Calculadora.Soma(n));
            Console.WriteLine("Subtracao: " + Calculadora.Subtracao(n));
            Console.WriteLine("Multiplicacao: " + Calculadora.Multiplicacao(n));
            Console.WriteLine("Divisao: " + Calculadora.Divisao(n));
        }
    }

    
}
