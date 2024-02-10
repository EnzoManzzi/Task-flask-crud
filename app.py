from flask import Flask 

app = Flask(__name__)

#CRUD
# Create  read, Updade and  delete = Criar, Ler, Atualizar e deletar
#tabela: Tarefa

task = []

@app.route  ('/task', methods=['POST'])
def Create_task():
    data = request.get_json()
    print(data)
    return 'Test'


if __name__ == "__main__":
    app.run(debug=True)