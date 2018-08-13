using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Batch1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")+" ***  START ***");
            log4net.Config.XmlConfigurator.Configure();
            FlightsEngine.Program.SearchFlights();
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  END ***");
            Console.WriteLine("Press Enter to exit.");
            Console.ReadLine();
        }
    }
}
