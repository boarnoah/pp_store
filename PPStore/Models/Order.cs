namespace PPStore.Models
{
    public class Order : BaseModel
    {
        public string Name { get; set; }
        public Address Address { get; set; }
        public Pizza Pizza { get; set; }
        public int PizzaCount { get; set; }
    }
}