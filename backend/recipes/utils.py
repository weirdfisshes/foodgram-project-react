from django.http import HttpResponse


def make_cart_file(ingredients):
    shopping_list = {}
    for ingredient in ingredients:
        amount = ingredient['total']
        name = ingredient['ingredient__name']
        measurement_unit = ingredient['ingredient__measurement_unit']
        shopping_list[name] = {
            'measurement_unit': measurement_unit,
            'amount': amount
        }
    main_list = ([f"{item}: {value['amount']}"
                  f" {value['measurement_unit']}\n"
                  for item, value in shopping_list.items()])
    response = HttpResponse(main_list, 'Content-Type: text/plain')
    response['Content-Disposition'] = 'attachment; filename="Cart.txt"'
    return response
