using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Batch1
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  START ***");
                log4net.Config.XmlConfigurator.Configure();
                FlightsEngine.Program.SearchFlights(ConfigurationManager.AppSettings["MainPythonScriptPath"], ConfigurationManager.AppSettings["PythonPath"]);
                Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  END ***");
                if (ConfigurationManager.AppSettings["ExitWhenFinished"] == "NO")
                {
                    Console.WriteLine("Press Enter to exit.");
                    Console.ReadLine();
                }
            }
            catch(Exception e)
            {
                Console.WriteLine("Error : "+e.ToString());
            }
        }
    }
}
