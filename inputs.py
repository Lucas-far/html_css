

"""
Módulo: inputs.py

Objetivo:
"""

def input_type_choice():
    """
    <div>
        <select id="questions" size="7" multiple>
            <option value="answer1">{% trans "Uma droga!" %}</option>
            <option value="answer2">{% trans "Tudo bem!" %}</option>
            <option value="answer3">{% trans "Uma maravilha!" %}</option>
            <option value="answer4">{% trans "Não sei dizer!" %}</option>
        </select>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="exampleFormControlSelect1">Campo para selecionar um gênero</label>
            <label>Escolha um gênero</label>
            <select class="form-control" id="exampleFormControlSelect1" name="gender">
                <option>escolher...</option>
                <option>feminino</option>
                <option>masculino</option>
                <option>outro</option>
            </select>
        </div>
    </div>
    """

def input_type_email():
    """
    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="email">Campo para escrever e-mail</label>
            <input type="email" class="form-control" id="email" max="100" min="2" name="email" placeholder="seu e-mail" size="20" required>
        </div>
    </div>
    """

def input_type_file():
    """
    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="avatar">Campo para fazer upload do seu avatar</label>
            <label>Forneça seu avatar</label>
            <input type="file" class="form-control-file" id="avatar" name="avatar">
        </div>
    </div>
    """

def input_type_number():
    """
    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="age">Campo para escrever idade</label>
            <input type="number" class="form-control" id="age" name="age" min="1" max="120" placeholder="sua idade" size="20" required>
        </div>
    </div>
    """

def input_type_password():
    """
    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="password">Campo para escrever senha</label>
            <input type="password" class="form-control" id="password" max="100" min="2" name="password" placeholder="sua senha" size="20" required>
        </div>
    </div>
    """

def input_type_text():
    """
    <div class="row mt-5">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="first_name">Campo para escrever o primeiro nome</label>
            <input type="text" class="form-control" id="first_name" max="100" min="2" name="first_name" placeholder="seu primeiro nome" size="20" required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="last_name">Campo para escrever o sobrenome</label>
            <input type="text" class="form-control" id="last_name" max="100" min="2" name="last_name" placeholder="seu sobrenome" size="20"  required>
        </div>
    </div>

    <div class="row">
        <div class="form-group ma mb-2">
            <label class="sr-only" for="username">Campo para escrever o nome de usuário/apelido</label>
            <input type="text" class="form-control" id="username" max="100" min="2" name="username" placeholder="seu nome de usuário" size="20" required>
        </div>
    </div>
    """

def input_type_textarea():
    """
    <div class="row">
        <div class="form-group ma mb-2 col-7 col-sm-7 col-md-7 col-lg-7 col-xl-7">
            <label class="sr-only" for="brief_description">Campo para falar algo sobre você</label>
            <textarea class="form-control" id="brief_description" name="brief_description" placeholder="Fale algo sobre você" rows="7" cols="40" required></textarea>
        </div>
    </div>
    """
