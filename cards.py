

"""
Módulo: cards.py

Palavra chave: exemplo de card
"""

# Tentativas de cards responsivos
def card():
    """
    <div class="container my-padding">
        <div class="row">
            {% for product in queryset %}
            <div class="col col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-5">
                <div class="card ma card-border">
                    <img src="{{ product.avatar.Thumb.url }}" class="card-img-top p-3" alt="...">
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
    """

def css():
    """
    .my-padding {margin-top: 100px;}
    .card {background-color: #292929; width: 17rem;}
    .card-border {border: #1ab7ea solid 1px; box-shadow: 0 0 25px #1ab7ea;}
    .inner-btn {border-radius: 0;}
    .inner-price {font-size: 1.5em; font-weight: bold;}
    .ma {margin: auto;}
    """
