from src.screens import telaInicial

infos = {}

t = telaInicial(infos)
while t.start:
    print(infos)
    t.menu()