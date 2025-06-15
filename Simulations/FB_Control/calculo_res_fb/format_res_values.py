# Nome do arquivo com os valores dos resistores
input_file = 'resistores.txt'
output_file = 'resistores_formatados.txt'

# Função para processar cada linha, removendo textos entre parênteses
def process_line(line):
    # Remove os valores entre parênteses
    import re
    cleaned_line = re.sub(r'\(.*?\)', '', line)
    # Remove espaços desnecessários e quebra a linha por vírgulas
    values = [value.strip() for value in cleaned_line.split(',') if value.strip()]
    return values

# Lê o arquivo e formata os valores
resistor_values = []
with open(input_file, 'r') as file:
    for line in file:
        resistor_values.extend(process_line(line))

# Formata os valores para o estilo desejado e salva no novo arquivo
with open(output_file, 'w') as file:
    file.write(', '.join(resistor_values) + '\n')

print(f"Valores formatados salvos em {output_file}")
