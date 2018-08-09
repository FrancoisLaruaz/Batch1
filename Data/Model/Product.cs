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
    
    public partial class Product
    {
        public int Id { get; set; }
        public System.DateTime CreationDate { get; set; }
        public System.DateTime ModificationDate { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public string ImageSrc { get; set; }
        public Nullable<decimal> Price { get; set; }
        public int SubTypeId { get; set; }
        public int StatusId { get; set; }
        public int UserId { get; set; }
        public int AddressId { get; set; }
    
        public virtual Address Address { get; set; }
        public virtual Category Category { get; set; }
        public virtual ProductSubType ProductSubType { get; set; }
        public virtual User User { get; set; }
    }
}
