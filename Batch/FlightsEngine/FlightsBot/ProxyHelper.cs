using IronPython.Hosting;
using System;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Scripting.Hosting;
using System.Diagnostics;
using System.IO;
using FlightsEngine.Models;
using System.Collections.Generic;
using System.Data.Linq;
using System.Data.Common;
using System.Linq;

namespace FlightsEngine.FlighsBot
{
    public static class ProxyHelper
    {
        // https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt


        public static List<string> CountriesToAvoid = new List<string>() { "CA", "US", "FR", "JP" ,"GB" ,"SE" ,"NO", "NE"};
        public static List<ProxyItem>  GetProxies()
        {
            List<ProxyItem> result = new List<ProxyItem>();
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  START Proxy Helper ***");
            try
            {
                ProxyItem item = new ProxyItem();
                item.Proxy = "82.214.139.109:8080 PL-N! -";
                item.CountryToAvoid = false;
                result.Add(item);

            }
            catch (Exception e)
            {
                FlightsEngine.Utils.Logger.GenerateError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);
            }
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  END Proxy Helper ***");
            return result;
        }

        public static string GetBestProxy(List<ProxyItem> Proxies)
        {
            string result = null;
            try
            {
                if (Proxies.Count > 0)
                {
                    int nbAttempts = Proxies.Sum(p => p.UseNumber);
                    if (nbAttempts < 1000)
                    {


                        List<ProxyItem> BaseList = null;
                        List<ProxyItem> ProxiesWithNoFailure = Proxies.FindAll(p => p.Failure == 0);
                        if (ProxiesWithNoFailure != null && ProxiesWithNoFailure.Count > 0)
                        {
                            List<ProxyItem> ProxiesWithNoFailureAndNotCountryToAvoid = ProxiesWithNoFailure.FindAll(p => p.CountryToAvoid == false);
                            if (ProxiesWithNoFailureAndNotCountryToAvoid != null && ProxiesWithNoFailure.Count > 0)
                            {
                                BaseList = ProxiesWithNoFailureAndNotCountryToAvoid;
                            }
                            else
                            {
                                BaseList = ProxiesWithNoFailure;
                            }
                            BaseList.Sort((x, y) => x.UseNumber.CompareTo(y.UseNumber));
                            result = Proxies[0].Proxy;
                        }
                        else
                        {
                            Proxies.Sort((x, y) => y.UseNumber.CompareTo(x.Failure));
                            result = Proxies[0].Proxy;
                        }
                    }
                }
            }
            catch (Exception e)
            {
                FlightsEngine.Utils.Logger.GenerateError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);
            }

            return result;
        }

    }
}