﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Web;
using FlightsEngine.Models;
using Transavia.Api.FlightOffers.Client;
using Transavia.Api.FlightOffers.Client.Model;
using System.Web.Script.Serialization;
using System.Net;
using FlightsEngine.Models.AirFranceKLM;
using FlightsEngine.Utils;

namespace FlightsEngine.FlighsAPI
{
    public static class AirFranceKLM
    {
        public static string Key = "jqgd23tz7qk7u7vu6ayes2w3";

        // Limits : 5/ second, 5000/day

        public static bool SearchFlights(AirlineSearch filter)
        {
            bool result = false;
            try
            {
                Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  START AirFranceKLM ***");
                MakeRequest(filter, AIRFranceKLMTravelHost.KL);
                MakeRequest(filter, AIRFranceKLMTravelHost.AF);
                Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  END AirFranceKLM ***");
            }
            catch (Exception e)
            {
                FlightsEngine.Utils.Logger.GenerateError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType,filter.ToSpecialString());
            }
            return result;
        }


        static bool MakeRequest(AirlineSearch filters, string TravelHost)
        {
            bool result = false;
            try
            {

                string url = "https://api.klm.com/opendata/flightoffers/available-offers";
                var httpWebRequest = (HttpWebRequest)WebRequest.Create(url);
                httpWebRequest.ContentType = "application/json";
                httpWebRequest.Method = "POST";
                httpWebRequest.Headers.Add("Accept-Language", "en-US");
                httpWebRequest.Headers.Add("AFKL-TRAVEL-Host", TravelHost);
                httpWebRequest.Headers.Add("Api-Key", Key);

                using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
                {
                    RequestBody body = new RequestBody();
                    body.passengerCount.ADULT = filters.AdultsNumber ;
                    body.passengerCount.CHILD = filters.ChildrenNumber;
                    body.passengerCount.INFANT = filters.BabiesNumber;
  

                    connection connection = new connection();
                    connection.departureDate = filters.FromDate.Value.ToString("yyyy-MM-dd");
                    if (!String.IsNullOrWhiteSpace(filters.FromAirportCode))
                        connection.origin.airport.code = filters.FromAirportCode;
                    if (!String.IsNullOrWhiteSpace(filters.ToAirportCode))
                        connection.destination.airport.code = filters.ToAirportCode;
                    body.requestedConnections.Add(connection);

                    if (filters.DirectFlightsOnly)
                    {
                        body.shortest = true;
                    }

                    if (filters.Return)
                    {
                        connection returnFlight = new connection();
                        returnFlight.departureDate = filters.ToDate.Value.ToString("yyyy-MM-dd");
                        if (!String.IsNullOrWhiteSpace(filters.FromAirportCode))
                            returnFlight.destination.airport.code = filters.FromAirportCode;
                        if (!String.IsNullOrWhiteSpace(filters.ToAirportCode))
                            returnFlight.origin.airport.code = filters.ToAirportCode;
                        body.requestedConnections.Add(returnFlight);
                    }

                    string json = new JavaScriptSerializer().Serialize(body);
                    streamWriter.Write(json);
                    streamWriter.Flush();
                    streamWriter.Close();
                }

                HttpWebResponse httpResponse = null;
                try
                {
                    result = true;
                    httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
                }
                catch (WebException e)
                {
                    result = false;
                    FlightsEngine.Utils.Logger.GenerateWebError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType,  filters.ToSpecialString());
                }

                if (result)
                {
                    using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
                    {
                        var requestResult = streamReader.ReadToEnd();

                        if (!String.IsNullOrWhiteSpace(requestResult))
                        {
                            JavaScriptSerializer srRequestResult = new JavaScriptSerializer();
                            dynamic jsondataRequestResult = srRequestResult.DeserializeObject(requestResult);
                            if (jsondataRequestResult != null && FlightsEngine.Utils.Utils.IsPropertyExist(jsondataRequestResult, ""))
                            {
                                result = true;
                            }
                        }
                    }
                }

            }
            catch (Exception e)
            {
                FlightsEngine.Utils.Logger.GenerateError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType, filters.ToSpecialString());
            }
            return result;
        }


    }
}
