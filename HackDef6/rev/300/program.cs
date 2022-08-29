using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace rev_300
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("rev_300");
            Console.ReadKey();
            Console.WriteLine("");
            connect_to_c2();
            Console.ReadKey();
        }

        public static void connect_to_c2()
        {
            Console.WriteLine("Funcion que se conecta al C2 para exfiltrar datos");
            Console.WriteLine("Preparando datos para exfiltrar...");

            string[] data = { "hackdef{", "_0f_", "!}", "_g00D_" , "nd1ng" };
            char und = Convert.ToChar(95);
            int di = 10;
            string qu = suma(di, -6);
            char am = Convert.ToChar(0x41);
            string t = suma(2, 1);
            string il = "SUxDT0RF";
            var base64EncodedBytes = System.Convert.FromBase64String(il);
            string IL = System.Text.Encoding.UTF8.GetString(base64EncodedBytes);
            string chi = suma(4, 1);
            string[] ars = { "h", "r", "t", "u", "v"};
            string flag = data[0] + ars[3] + und + ars[0] + qu + ars[4] + t + und + am + data[3] + "und" + t + ars[1] + chi + ars[2] + qu + data[4] + data[1] + IL + data[2];
            Console.WriteLine(flag);

        }

        public static string suma(int x, int y)
        {
            int z;
            z = x + y;
            return z.ToString();
        }
    }
}
