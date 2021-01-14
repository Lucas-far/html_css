

"""
Módulo: cards.py

Palavra chave: card responsivo
"""

# Tentativas de cards responsivos
def card():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="#" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>

        <style>
            body {background-color: #222; color: silver; font-family: gothic;}
            .card {background-color: #292929; width: 15rem;}
            .inner-btn {border-radius: 0;}
            .inner-price {font-size: 2em; font-weight: bold;}
            .ma {margin: auto;}
        </style>

    </head>

    <body>

        <div class="container mt-5">
            <div class="row">
                {% for product in queryset %}
                <div class="col col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-5">
                    <div class="card ma">
                        <img src="{{ product.avatar.Thumb.url }}" class="card-img-top" alt="...">
                        <div class="card-body text-center">
                            <h5 class="card-title">{{ product.name }}</h5>
                            <p class="card-text"></p>
                            <a href="#" class="btn btn-danger inner-btn">Add to cart</a>
                            <a href="#" class="btn btn-secondary inner-btn">View</a>
                            <span class="inner-price">R${{ product.price }}</span>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>

    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """
