namespace PPStore.Models
{
    public class Pizza : BaseModel
    {
        public string Name { get; set; }
        public int Price { get; set; }
        public string DescriptionShort { get; set; }
        public string DescriptionLong { get; set; }
    }
}