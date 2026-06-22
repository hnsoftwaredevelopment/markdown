Create JSON using Collection Initializers

Create JSON using Collection Initializers

```C#
JObject o = new JObject
{
    { "Cpu", "Intel" },
    { "Memory", 32 },
    {
        "Drives", new JArray
        {
            "DVD",
            "SSD"
        }
    }
};

Console.WriteLine(o.ToString());
// {
//   "Cpu": "Intel",
//   "Memory": 32,
//   "Drives": [
//     "DVD",
//     "SSD"
//   ]
// }
```