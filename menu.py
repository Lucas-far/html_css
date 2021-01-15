

"""
Módulo: menu.py

Palavra chave: exemplo de menu
"""

# Template do menu
def menu():
    """
    <div class="container-fluid fix-this-area">
        <div class="row">
            <div class="col">
                <div class="nav-item dropdown text-right">
                    <span class="logo">Logo</span>
                    <button class="btn my-btn">
                        <a aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle my-a" data-toggle="dropdown" href="#" id="navbarDropdown" role="button">
                            Menu
                        </a>
                        <span aria-labelledby="navbarDropdown" class="dropdown-menu">
                            <a class="dropdown-item" href="#">Item 1</a>
                            <a class="dropdown-item" href="#">Item 2</a>
                            <a class="dropdown-item" href="#">Item 3</a>
                            <a class="dropdown-item" href="#">Item 4</a>
                            <a class="dropdown-item" href="#">Item 5</a>
                        </span>
                    </button>
                </div>
            </div>
        </div>
    </div>
    """

# Css do template do menu
def css():
    """
    .fix-this-area {
        position: fixed;
        top: 0;
        background-color: #444;
        width: 100%;
        z-index: 1;
    }

    .logo {float: left; font-size: 2em;}
    .dropdown-item {text-align: right;}
    .dropdown-menu {background-color: #444; width: 200%;}
    """
