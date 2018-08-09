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
    
    public partial class User
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public User()
        {
            this.EmailAudits = new HashSet<EmailAudit>();
            this.News = new HashSet<News>();
            this.Products = new HashSet<Product>();
            this.ScheduledTasks = new HashSet<ScheduledTask>();
            this.SearchResults = new HashSet<SearchResult>();
            this.UserFollows = new HashSet<UserFollow>();
            this.UserFollows1 = new HashSet<UserFollow>();
        }
    
        public int Id { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Description { get; set; }
        public Nullable<System.DateTime> DateOfBirth { get; set; }
        public int LanguageId { get; set; }
        public string PictureSrc { get; set; }
        public bool ReceiveNews { get; set; }
        public string PictureThumbnailSrc { get; set; }
        public Nullable<int> GenderId { get; set; }
        public string ResetPasswordToken { get; set; }
        public string EmailConfirmationToken { get; set; }
        public System.DateTime DateLastConnection { get; set; }
        public System.DateTime ModificationDate { get; set; }
        public System.DateTime CreationDate { get; set; }
        public string AspNetUserId { get; set; }
        public string UserNameModification { get; set; }
        public bool PublicProfile { get; set; }
        public string FacebookLink { get; set; }
        public string BackgroundPictureSrc { get; set; }
        public Nullable<int> AddressId { get; set; }
    
        public virtual Address Address { get; set; }
        public virtual AspNetUser AspNetUser { get; set; }
        public virtual Category Category { get; set; }
        public virtual Category Category1 { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<EmailAudit> EmailAudits { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<News> News { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Product> Products { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<ScheduledTask> ScheduledTasks { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<SearchResult> SearchResults { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<UserFollow> UserFollows { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<UserFollow> UserFollows1 { get; set; }
    }
}
