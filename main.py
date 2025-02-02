# Importando bibliotecas
import os
import tkinter
import customtkinter
from PIL import Image
import customtkinter as ctk

# Definindo variaveis
filePasta         = "resultados"
fileAprovado      = "resultados/aprovados.txt"
fileReprovado     = "resultados/reprovados.txt"

# Definindo funções
def openInterface():
    # Quando o botão "Registrar" for pressionado
    def buttonRegisterResponse():
        if not os.path.isdir(filePasta):
            os.makedirs(filePasta, exist_ok=True)

        if comboboxType.get() == " Aprovado":
            if os.path.exists(fileAprovado):
                with open(fileAprovado, 'a') as file:
                    file.write("|-----------| APROVADO |-----------|\n| ID: {}\n| Nome: {}\n| Discord: {}\n| WhatsApp: {}\n|----------------------------------|\n\n"
                                  .format(entryForm.get(), entryNome.get(), entryDiscord.get(), entryWhats.get()))
            else:
                with open(fileAprovado, 'w') as file:
                    file.write("|-----------| APROVADO |-----------|\n| ID: {}\n| Nome: {}\n| Discord: {}\n| WhatsApp: {}\n|----------------------------------|\n\n"
                                  .format(entryForm.get(), entryNome.get(), entryDiscord.get(), entryWhats.get()))
                    
        else:
            if os.path.exists(fileReprovado):
                with open(fileReprovado, 'a') as file:
                    file.write("|-----------| REPROVADO |-----------|\n| ID: {}\n| Nome: {}\n| Discord: {}\n| WhatsApp: {}\n|-----------------------------------|\n\n"
                                  .format(entryForm.get(), entryNome.get(), entryDiscord.get(), entryWhats.get()))
            else:
                with open(fileReprovado, 'a') as file:
                    file.write("|-----------| REPROVADO |-----------|\n| ID: {}\n| Nome: {}\n| Discord: {}\n| WhatsApp: {}\n|-----------------------------------|\n\n"
                                .format(entryForm.get(), entryNome.get(), entryDiscord.get(), entryWhats.get()))
                    
        buttonClearResponse()

    # Quando o botão "Limpar" for pressionado
    def buttonResetResponse():
        if not os.path.isdir(filePasta):
            os.makedirs(filePasta, exist_ok=True)

        if comboboxType.get() == " Aprovado":
            if os.path.exists(fileAprovado):
                os.remove(fileAprovado)

                with open(fileAprovado, 'a') as file:
                    file.write("")
            else:
                with open(fileAprovado, 'a') as file:
                    file.write("")

            
        else:
            if os.path.exists(fileReprovado):
                os.remove(fileReprovado)

                with open(fileReprovado, 'a') as file:
                    file.write("")
            else:
                with open(fileReprovado, 'a') as file:
                    file.write("")

    # Quando o botão "Resetar" for pressionado
    def buttonClearResponse():
        entryForm.delete(0, customtkinter.END)  # Limpa o conteúdo da entrada
        entryForm.selection_clear()  # Remove a seleção do texto
        entryForm.configure(placeholder_text="ID")  # Garante que o placeholder seja mostrado novamente
        root.focus()
    
        entryNome.delete(0, customtkinter.END)  # Limpa o conteúdo da entrada
        entryNome.selection_clear()  # Remove a seleção do texto
        entryNome.configure(placeholder_text="Nome")  # Garante que o placeholder seja mostrado novamente
        root.focus()
        
        entryDiscord.delete(0, customtkinter.END)  # Limpa o conteúdo da entrada
        entryDiscord.selection_clear()  # Remove a seleção do texto
        entryDiscord.configure(placeholder_text="Discord")  # Garante que o placeholder seja mostrado novamente
        root.focus()
                
        entryWhats.delete(0, customtkinter.END)  # Limpa o conteúdo da entrada
        entryWhats.selection_clear()  # Remove a seleção do texto
        entryWhats.configure(placeholder_text="WhatsApp")  # Garante que o placeholder seja mostrado novamente
        root.focus()

        comboboxType.set(" Aprovado") # Setar o texto do combobox para "Aprovado"

    # Configurando o modo e o tema da interface
    customtkinter.set_appearance_mode("System")  # Modo de aparência do sistema (claro ou escuro)
    customtkinter.set_default_color_theme("green")  # Definindo o tema de cores como "verde"

    # Criando a janela principal da interface
    root = customtkinter.CTk()  # Instância da janela principal (CTk)
    root.geometry("1024x720")  # Definindo o tamanho da janela (1024x720 pixels)
    root.resizable(False, False)  # Desabilitando o redimensionamento da janela
    root.title('Formulario Automatizado')  # Definindo o título da janela
    if os.path.exists("assets/bitmap.ico"):
        root.iconbitmap("assets/bitmap.ico") # Definindo o icone da janela

    # Carregando a imagem de fundo com a biblioteca PIL
    if os.path.exists("assets/background.png"):
        imageBackground = Image.open("assets/background.png")  # Abrindo a imagem de fundo

    # Convertendo a imagem para um formato compatível com customtkinter (CTkImage)
    if os.path.exists("assets/background.png"):
        ctk_imageBackground = ctk.CTkImage(imageBackground, size=(1024, 720))  # Ajustando o tamanho da imagem de fundo

    # Criando o Label para exibir a imagem de fundo
    if os.path.exists("assets/background.png"):
        labelBackground = customtkinter.CTkLabel(master=root, image=ctk_imageBackground)
    else:
        labelBackground = customtkinter.CTkLabel(master=root)
    labelBackground.pack(fill=tkinter.BOTH, expand=True)  # Fazendo a imagem preencher toda a janela

    # Criando um frame (caixa) sobre a imagem de fundo
    frameBackground = customtkinter.CTkFrame(master=labelBackground, width=620, height=480, corner_radius=20)
    frameBackground.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)  # Centralizando o frame na janela

    # Adicionando texto com a versão do formulário na parte superior
    labelText = ctk.CTkLabel(master=root, text="v1.0 (By Kauan T.)", font=('Century Gothic', 15))
    labelText.place(x=10, y=5)  # Posicionando o texto no canto superior esquerdo

    # Adicionando o título "Formulario Automatizado" dentro do frame
    labelText = customtkinter.CTkLabel(master=frameBackground, text="Formulario Automatizado", font=('Century Gothic', 25))
    labelText.place(x=165, y=30 + 35)  # Posicionando o título dentro do frame

    # Obtendo a cor de fundo do frame
    labelColor = frameBackground.cget("fg_color")  # Pegando a cor de fundo do frame para usar nos outros elementos

    # Criando uma linha horizontal (frame linear) abaixo do título
    frameLinear = customtkinter.CTkFrame(master=labelBackground, width=500, height=2, corner_radius=20, fg_color="#343638", bg_color=labelColor)
    frameLinear.place(x=265, y=195 + 35)  # Posicionando a linha abaixo do título

    # Criando o campo de entrada para o "ID"
    entryForm = customtkinter.CTkEntry(master=labelBackground, width=100, height=35, placeholder_text="ID", bg_color=labelColor, corner_radius=0, font=('Century Gothic', 15))
    entryForm.place(x=265, y=220 + 35)  # Posicionando o campo de entrada do ID

    # Criando o campo de entrada para o "Nome"
    entryNome = customtkinter.CTkEntry(master=labelBackground, width=385, height=35, placeholder_text="Nome", bg_color=labelColor, corner_radius=0, font=('Century Gothic', 15))
    entryNome.place(x=380, y=220 + 35)  # Posicionando o campo de entrada do Nome

    # Criando o campo de entrada para o "Discord"
    entryDiscord = customtkinter.CTkEntry(master=labelBackground, width=241, height=35, placeholder_text="Discord", bg_color=labelColor, corner_radius=0, font=('Century Gothic', 15))
    entryDiscord.place(x=265, y=270 + 35)  # Posicionando o campo de entrada do Discord

    # Criando o campo de entrada para o "WhatsApp"
    entryWhats = customtkinter.CTkEntry(master=labelBackground, width=240, height=35, placeholder_text="WhatsApp", bg_color=labelColor, corner_radius=0, font=('Century Gothic', 15))
    entryWhats.place(x=523, y=270 + 35)  # Posicionando o campo de entrada do WhatsApp

    # Criando uma caixa de seleção (combobox) para escolher entre "Aprovados" ou "Reprovados"
    comboboxType = customtkinter.CTkComboBox(master=labelBackground, values=[" Aprovado", " Reprovado"], width=130, height=35, text_color="#94948c", bg_color=labelColor, corner_radius=0, font=('Century Gothic', 15))
    comboboxType.place(x=632, y=320 + 35)  # Posicionando a caixa de seleção

    # Criando outra linha horizontal (frame linear) abaixo da caixa de seleção
    frameLinearDown = customtkinter.CTkFrame(master=labelBackground, width=500, height=2, corner_radius=20, fg_color="#343638", bg_color=labelColor)
    frameLinearDown.place(x=265, y=370 + 35)  # Posicionando a linha abaixo da caixa de seleção

    # Criando o botão de "Registrar"
    buttonRegister = customtkinter.CTkButton(master=labelBackground, text="Registrar", width=499, height=35, corner_radius=0, fg_color="#2fa571", font=('Century Gothic', 15), command=buttonRegisterResponse)
    buttonRegister.place(x=265, y=395 + 40)  # Posicionando o botão de registrar

    # Criando o botão de "Limpar"
    buttonClear = customtkinter.CTkButton(master=labelBackground, text="Limpar", width=240, height=35, corner_radius=0, fg_color="#e86e6d", font=('Century Gothic', 15), command=buttonClearResponse, hover_color="#f04c50")
    buttonClear.place(x=265, y=442 + 40)  # Posicionando o botão de limpar

    # Criando o botão de "Resetar"
    buttonReset = customtkinter.CTkButton(master=labelBackground, text="Resetar", width=240, height=35, corner_radius=0, fg_color="#e86e6d", font=('Century Gothic', 15), command=buttonResetResponse, hover_color="#f04c50")
    buttonReset.place(x=523, y=442 + 40)  # Posicionando o botão de resetar

    # Iniciando a interface gráfica
    root.mainloop()  # Inicia o loop principal da interfaces

# Verificar se esta sendo executado diretamente
if __name__ == "__main__":
    openInterface()