import os

# Define quais pastas e subpastas devem ser criados
diretorios = [
    "Digix/assets/css/admin",
    "Digix/assets/css/colaborador",
    "Digix/assets/js/admin",
    "Digix/assets/js/colaborador",
    "Digix/assets/images",
    "Digix/assets/fonts",
    "Digix/components",
    "Digix/login",
    "Digix/admin/usuario",
    "Digix/admin/produtos",
    "Digix/admin/desafios",
    "Digix/admin/pedidos",
    "Digix/admin/relatorios",
    "Digix/colaborador/usuario",
    "Digix/colaborador/ranking",
    "Digix/colaborador/produtos",
    "Digix/colaborador/carrinho",
    "Digix/colaborador/desafios",
    "Digix/utils",
    "Digix/data",
    "Digix/api/app/Controllers",
    "Digix/api/app/Models",
    "Digix/api/app/Views",
    "Digix/api/app/Services",
    "Digix/api/app/Helpers",
    "Digix/api/config",
    "Digix/api/public",
    "Digix/api/routes",
    "Digix/api/storage/logs",
    "Digix/api/storage/uploads",
    "Digix/api/tests",
    "Digix/api/vendor"
]

for dir in diretorios:
    os.makedirs('../'+dir, exist_ok=True)
    with open(os.path.join(dir, '.gitkeep'), 'w') as f:
        pass

print("Diretórios e .gitkeep files creados com sucesso.")
