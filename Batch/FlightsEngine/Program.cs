using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using FlightsEngine.FlighsAPI;
using FlightsEngine.Models;

namespace FlightsEngine
{
    public static class Program
    {
        public static  bool SearchFlights(string MainPythonScriptPath,string PythonPath)
        {
            bool result = false;
            try
            {
                AirlineSearch filter1 = new AirlineSearch();
                filter1.FromAirportCode = "AMS";
                filter1.FromDate = new DateTime(2018, 10, 20);
                filter1.ToAirportCode = "BCN";
                filter1.Return = true;
                filter1.ToDate = new DateTime(2018, 10, 28);
                filter1.AdultsNumber = 1;
                filter1.DirectFlightsOnly = true;

                string Proxy = "185.188.191.247:21776 SK-H-S +";
                ScrappingSearch scrappingSearch = new ScrappingSearch();
                scrappingSearch.Proxy = Proxy;
                scrappingSearch.PythonPath = PythonPath;
                scrappingSearch.MainPythonScriptPath = MainPythonScriptPath;
                scrappingSearch.SearchTripProviderId = 1;
                scrappingSearch.Provider = "Edreams";

                Task.Factory.StartNew(() =>  FlighsBot.PythonHelper.Run(filter1, scrappingSearch));
                Task.Factory.StartNew(() => FlighsBot.PythonHelper.Run(filter1, scrappingSearch));
                // Console.WriteLine("Pythonresult = "+ Pythonresult.Success+" and Error = "+ (Pythonresult.Error??""));

                //   FlighsBot.Kayak.SearchFlights(filter1);
                //   FlighsBot.Kayak.SearchFlights(filter1);

                //   FlightsEngine.FlighsAPI.AirFranceKLM.SearchFlights(filter1);
                //    FlightsEngine.FlighsAPI.AirHob.SearchFlights(filter1);
                //   FlightsEngine.FlighsAPI.Kiwi.SearchFlights(filter1);
                // FlightsEngine.FlighsAPI.RyanAir.SearchFlights(filter1);
                //  FlightsEngine.FlighsAPI.Transavia.SearchFlights(filter1);
            }
            catch(Exception e)
            {
                FlightsEngine.Utils.Logger.GenerateError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);
            }
            return result;
        }

        public static void SearchFlights(object p1, object p2, object p3)
        {
            throw new NotImplementedException();
        }
    }
}
