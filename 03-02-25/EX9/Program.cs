namespace EX9
{
    internal class Carro
    {
        public string Marca { get; set; }
        public string Modelo { get; set; }
        public string Ano { get; set; }

    }
    internal class Program
    {
        static void Main(string[] args)
        {
            var Carro = new Carro();
            Console.Write("Marca: ");
            Carro.Marca = Console.ReadLine();
            Console.Write("Modelo: ");
            Carro.Modelo = Console.ReadLine();
            Console.Write("Ano: ");
            Carro.Ano = Console.ReadLine();
            Console.Clear();
            Console.WriteLine("OUTPUT: ");
            Console.WriteLine("Marca: " + Carro.Marca);
            Console.WriteLine("Modelo: " + Carro.Modelo);
            Console.WriteLine("Ano: " + Carro.Ano);
        }
    }
}
