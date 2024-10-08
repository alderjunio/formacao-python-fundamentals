def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Terça Feira, 08 de Outubro de 2024", 
             "O amor, quando se revela", 
             "Não se sabe revelar", 
             "Sabe bem olhar p'ra ela", 
             "mas não lhe sabe falar",            
             author="Fernando Pessoa", ano=1999)    