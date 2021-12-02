from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TABLE_HEAD = """
                <table class="table">
                    <tbody>
             """
TABLE_TAIL = """
                   </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                        <td>{name}</td>
                        <td>{value}</td>
                    </tr>
                """
PRODUCT_SPEC = {
    'notebook': {
        'Частота процессора': 'product.processor_freq',
        'Диагональ': 'product.diagonal',
        'Тип дисплея': 'product.display_type',
        'Оперативная память': 'product.ram',
        'Видеокарта': 'product.video',
        'Время работы': 'product.time_without_charge',
    },
    'smartphone': {
        'Диагональ': 'product.diagonal',
        'Тип дисплея': 'product.display_type',
        'Разрешение экрана': 'product.resolution',
        'Емкость батареи': 'product.accum_volume',
        'Оперативная память': 'product.ram',
        'Обьем памяти': 'product.sd_volume_max',
        'Камера Главная': 'product.mini_cam_mp',
        'Фронтальная камера': 'product.frontal_cam_mp',
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter()
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
