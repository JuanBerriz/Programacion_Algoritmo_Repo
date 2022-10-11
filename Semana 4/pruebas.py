
def estadisticas(id_comp):
    for games in estadistica:
        for key,value in games.items():
            if key == "id" and value == id_comp:
                games["Cantidad Vendida"] += 1
            else:
                continue
    return

estadistica = [
        {
        "id": 1,
        "name": "Overwatch2",
        "Cantidad Vendida": 0  
        },

        {
        "id": 2,
        "name": "Valorant",
        "Cantidad Vendida": 0
        },

        {
        "id": 3,
        "name": "Pixel Gun 3D",
        "Cantidad Vendida": 0 
        },

        {
        "id": 4,
        "name": "Pokemon",
        "Cantidad Vendida": 0  
        },

        {
        "id": 5,
        "name": "Final Fantasy Exvius",
        "Cantidad Vendida": 0 
        },

        {
        "id": 6,
        "name": "Minecraft",
        "Cantidad Vendida": 0  
        },
        
        {
        "id": 7,
        "name": "Cyberpunk 2077",
        "Cantidad Vendida": 0 
        },

        {
        "id": 8,
        "name": "GTA V",
        "Cantidad Vendida": 0 
        } 
]

while True:
    id_comp = int(input("ID:"))
    estadisticas(id_comp)
    if id_comp == 0:
        break

print(estadistica)