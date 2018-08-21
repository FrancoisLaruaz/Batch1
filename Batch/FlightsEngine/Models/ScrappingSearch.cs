using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightsEngine.Models
{
    public class ScrappingSearch
    {
        public ScrappingSearch()
        {

        }

        public string Proxy { get; set; }

        public string Provider { get; set; }

        public string MainPythonScriptPath { get; set; }

        public string PythonPath { get; set; }


        public int SearchTripProviderId { get; set; }


    }
}
