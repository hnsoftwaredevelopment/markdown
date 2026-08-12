Create JSON object with dynamic

Create JSON object with dynamic
```C#
dynamic product = new JObject();
product.ProductName = "Elbow Grease";
product.Enabled = true;
product.Price = 4.90m;
product.StockCount = 9000;
product.StockValue = 44100;
product.Tags = new JArray("Real", "OnSale");

Console.WriteLine(product.ToString());
// {
//   "ProductName": "Elbow Grease",
//   "Enabled": true,
//   "Price": 4.90,
//   "StockCount": 9000,
//   "StockValue": 44100,
//   "Tags": [
//     "Real",
//     "OnSale"
//   ]
// }
```