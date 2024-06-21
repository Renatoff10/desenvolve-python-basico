import emoji

# Lista de emojis disponíveis
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Exibe a lista de emojis disponíveis
print("Emojis disponíveis:")
for visual, codigo in emojis_disponiveis.items():
    print(f"{visual} - {codigo}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("Digite uma frase e ela será emojizada: ")

# Decodifica e exibe a frase com os emojis
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)
print(f"Frase emojizada:\n{frase_emojizada}")
