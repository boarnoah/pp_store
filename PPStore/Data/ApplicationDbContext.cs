using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using PPStore.Models;

namespace PPStore.Data
{
    public class ApplicationDbContext : IdentityDbContext
    {
        public DbSet<Pizza> Pizzas { get; set; }
     
        public DbSet<Order> Orders { get; set; }
        public DbSet<Address> Address { get; set; }
     


        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {

        }
    }
}
