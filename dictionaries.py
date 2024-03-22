capitals = {"kenya": "nairobi",
            "USA": "washington DC",
            "germany": "berlin",
            "somalia": "mogadishu",
            "ethiopia": "adiss ababa",
            "djibouti": "djibouti",
            "uganda": "kampala"}
#knowing the attributes print(dir(capitals))
#attributes description print(help(capitals))
print(capitals.get("kenya"))
capitals.update({"tanzania": "tanganyika"})
print(capitals)
capitals.pop("kenya")
print(capitals)
capitals.popitem()
print(capitals)
