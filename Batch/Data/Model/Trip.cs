//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace Data.Model
{
    using System;
    using System.Collections.Generic;
    
    public partial class Trip
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public Trip()
        {
            this.Flights = new HashSet<Flight>();
        }
    
        public int Id { get; set; }
        public Nullable<int> CurrencyId { get; set; }
        public decimal Price { get; set; }
        public string Url { get; set; }
        public int SearchTripProviderId { get; set; }
        public Nullable<decimal> EuroPrice { get; set; }
    
        public virtual Currency Currency { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Flight> Flights { get; set; }
        public virtual SearchTripProvider SearchTripProvider { get; set; }
    }
}
