﻿using IronPython.Hosting;
using System;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Scripting.Hosting;
using System.Diagnostics;
using System.IO;
using FlightsEngine.Models;
using System.Collections.Generic;
using FlightsEngine.Utils;

namespace FlightsEngine.FlighsBot
{
    public static class PythonHelper
    {
        public static PythonExecutionResult Run(AirlineSearch filter, ScrappingSearch scrappingSearch)
        {
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  START Python Helper ***");
            PythonExecutionResult result = new PythonExecutionResult();
            System.Diagnostics.Process cmd = new System.Diagnostics.Process();
            try
            {
                // https://stackoverflow.com/questions/1469764/run-command-prompt-commands


                string args = "\""+ scrappingSearch.Proxy + "\" \""+ scrappingSearch.SearchTripProviderId + "\" \"" + scrappingSearch.Provider + "\" \""+ filter.FromAirportCode + "\" \"" + filter.ToAirportCode + "\" \"" + filter.DirectFlightsOnly.ToString().ToLower() + "\" \""+filter.FromDate.Value.ToString("dd'/'MM'/'yyyy") +"\"";
                if(filter.Return)
                {
                    args=args + " \"" + filter.ToDate.Value.ToString("dd'/'MM'/'yyyy") + "\"";
                }


                System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
                startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
                startInfo.FileName = "cmd.exe";
                startInfo.Arguments = string.Format("/C {0} {1} {2}", scrappingSearch.PythonPath, scrappingSearch.MainPythonScriptPath, args);

                startInfo.RedirectStandardInput = true;
                startInfo.RedirectStandardOutput = true;
                cmd.StartInfo.CreateNoWindow = false;
                startInfo.UseShellExecute = false; ;
                /*
                start.UseShellExecute = false;// Do not use OS shell
                start.CreateNoWindow = true; // We don't need new window
                start.RedirectStandardOutput = true;// Any output, generated by application will be redirected back
                start.RedirectStandardError = true; // Any error in standard output will be redirected back (for example exceptions)
                */
                cmd.StartInfo = startInfo;
                cmd.Start();
                string strResult = "";
                List<string> resultList = new List<string>();
                while (!cmd.StandardOutput.EndOfStream)
                {
                    strResult = cmd.StandardOutput.ReadLine();
                    resultList.Add(strResult);
                }

                if (!String.IsNullOrWhiteSpace(strResult))
                {
                    if (strResult.StartsWith("OK"))
                    {
                        result.Success = true;
                    }
                    else
                    {

                        if (strResult.Contains("|"))
                        {
                            result.Error = strResult.Split('|')[1];
                        }
                        if (result.Error==null || result.Error.ToLower() != PythonError.WebdriverTimeout.ToLower())
                        {
                            foreach (string log in resultList)
                            {
                                Console.WriteLine(log);
                            }
                        }
                    }
                }
            }
            catch (Exception e)
            {
                result.Success = false;
                result.Error = e.ToString();
                FlightsEngine.Utils.Logger.GenerateError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType, "Provider = " + scrappingSearch.Provider + " and Proxy = " + scrappingSearch.Proxy + " and filters = "+filter.ToSpecialString());
            }
            finally
            {
                cmd.StandardInput.WriteLine("exit");
                cmd.WaitForExit();
                cmd.Close();
            }
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  END Python Helper ***");
            return result;
        }

    }
}