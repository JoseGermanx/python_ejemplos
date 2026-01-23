calorias = [120, 180, 250, 310, 420]


recomendaciones = list(
    map(
        lambda c: "Snack liviano" if c < 150 else
                  "Barrita energética" if c <= 300 else
                  "Smoothie o batido",
        calorias
    )
)

print(recomendaciones)


intensos = list(filter(lambda c: c > 300, calorias))
print(intensos)
