using System;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FlightsEngine.FlighsBot
{
    public static class Test
    {
        public static void run()
        {

            // https://www.youtube.com/watch?v=PYnWKSXXyIk
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  START Test ***");
            var task = MessageLoopWorker.Run(DoWorkAsync,
                "https://www.ca.kayak.com/horizon/sem/flights/general");
            task.Wait();
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " ***  END Test ***");
        }

        static void ClickElement(HtmlElement element, WebBrowser wb)
        {
            if (wb.InvokeRequired)
            {
                wb.BeginInvoke((MethodInvoker)delegate ()
                {
                    ClickElement(element, wb);
                });
            }
            else
            {
                element.InvokeMember("click");
            }
        }

        static HtmlElement GetHtmlElementByEndOfId(string endOfId, string tagName, WebBrowser wb)
        {
            HtmlElement result = null;

            try
            {
                var elements = wb.Document.GetElementsByTagName(tagName);
                foreach (HtmlElement e in elements)
                {
                    if ( (e.Id != null && e.Id.EndsWith(endOfId)))
                    {
                        result = e;
                        break;
                    }
                }
            }
            catch (Exception e)
            {
                FlightsEngine.Utils.Logger.GenerateError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType, "endOfId =" + endOfId + " and webbrowser =" + (wb?.Url?.ToString() ?? "[NULL]"));
            }

            return result;
        }

        static HtmlElement GetHtmlElementByClass(string className,string tagName, WebBrowser wb)
        {
            HtmlElement result = null;

            try
            {
                var elements = wb.Document.GetElementsByTagName(tagName);
                foreach (HtmlElement e in elements)
                {
                    string _elementClass = e.GetAttribute("className");
                    if (_elementClass == className )
                    {
                        result = e;
                        break;
                    }
                }
            }
            catch(Exception e)
            {
                FlightsEngine.Utils.Logger.GenerateError(e, System.Reflection.MethodBase.GetCurrentMethod().DeclaringType, "className ="+ className+" and webbrowser ="+ (wb?.Url?.ToString() ?? "[NULL]"));
            }

            return result;
        }



        // navigate WebBrowser to the list of urls in a loop
        static async Task<object> DoWorkAsync(object[] args)
        {
            Console.WriteLine("Start working.");

            using (var wb = new WebBrowser())
            {
                wb.ScriptErrorsSuppressed = true;
                wb.AllowNavigation = true;

                TaskCompletionSource<bool> tcs = null;
                WebBrowserDocumentCompletedEventHandler documentCompletedHandler = (s, e) =>
                  {
                      var document = ((WebBrowser)wb).Document;
                      var documentAsIHtmlDocument3 = (mshtml.IHTMLDocument3)document.DomDocument;
                      var content = documentAsIHtmlDocument3.documentElement.innerHTML;
                      WebBrowser _wb=((WebBrowser)s);
                      HtmlElement origin= GetHtmlElementByEndOfId("-origin", "input", _wb);
                      origin.SetAttribute("value", "AMS");

                      HtmlElement destination = GetHtmlElementByEndOfId("-destination", "input", _wb);
                      origin.SetAttribute("value", "BCN");

                      HtmlElement clickableElement =  GetHtmlElementByEndOfId("-submit", "button", _wb);

                      HtmlElement returnDate = GetHtmlElementByEndOfId("-return-input", "input", _wb);
                      origin.SetAttribute("value", "18/08/2018");

                      HtmlElement departDate = GetHtmlElementByEndOfId("-depart-input", "input", _wb);
                      origin.SetAttribute("value", "10/08/2018");


                      if (clickableElement != null)
                      {
                          // clickableElement.InvokeMember("click");
                          ClickElement(clickableElement, _wb);
                          /*
                          while (true)
                          {
                              System.Windows.Forms.Application.DoEvents();
                              if (GetHtmlElementByClass("best-flights-header", "div", wb) != null)
                                  break;
                          }
                          */
                          Thread.Sleep(10000);

                          _wb.Document.GetElementById("best-flights-header").InvokeMember("Click");

                      }
                      tcs.TrySetResult(true);
                  };

                // navigate to each URL in the list
                foreach (var url in args)
                {
                    tcs = new TaskCompletionSource<bool>();
                    wb.DocumentCompleted += documentCompletedHandler;
                    try
                    {
                        wb.Navigate(url.ToString());
                        // await for DocumentCompleted
                        await tcs.Task;
                    }
                    finally
                    {
                        wb.DocumentCompleted -= documentCompletedHandler;
                    }
                    // the DOM is ready
                    Console.WriteLine(url.ToString());
                    Console.WriteLine(wb.Document.Body.OuterHtml);
                }
            }

            Console.WriteLine("End working.");
            return null;
        }

    }

    // a helper class to start the message loop and execute an asynchronous task
    public static class MessageLoopWorker
    {
        public static async Task<object> Run(Func<object[], Task<object>> worker, params object[] args)
        {
            var tcs = new TaskCompletionSource<object>();

            var thread = new Thread(() =>
            {
                EventHandler idleHandler = null;

                idleHandler = async (s, e) =>
                {
                    // handle Application.Idle just once
                    Application.Idle -= idleHandler;

                    // return to the message loop
                    await Task.Yield();

                    // and continue asynchronously
                    // propogate the result or exception
                    try
                    {
                        var result = await worker(args);
                        tcs.SetResult(result);
                    }
                    catch (Exception ex)
                    {
                        tcs.SetException(ex);
                    }

                    // signal to exit the message loop
                    // Application.Run will exit at this point
                    Application.ExitThread();
                };

                // handle Application.Idle just once
                // to make sure we're inside the message loop
                // and SynchronizationContext has been correctly installed
                Application.Idle += idleHandler;
                Application.Run();
            });

            // set STA model for the new thread
            thread.SetApartmentState(ApartmentState.STA);

            // start the thread and await for the task
            thread.Start();
            try
            {
                return await tcs.Task;
            }
            finally
            {
                thread.Join();
            }
        }
    }
}