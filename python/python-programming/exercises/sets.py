set1 = {"hola", "buenos","dias", "uno","dos", "tres", "cuatro"}
set2 = {"hola", "buenas","tardes", "uno","cinco", "seis","siete", "ocho"}


def run():
    set_union = set1 | set2
    print(f' Set union:  {set_union}')

    set_interseccion = set1 & set2
    print(f' Set Interseccion:  {set_interseccion}')

    set_diferencia = set1 - set2
    print(f' Set diferencia:  {set_diferencia}')

    set_dif_simetrica = set1 ^ set2
    print(f' Set dif simetrica:  {set_dif_simetrica}')

if __name__ == '__main__':
    run()