import sys

import any
import collection
import custom_class_serializer
import custom_field_serializer
import default
import env
import flatten
import forward_reference
import generics
import jsonfile
import lazy_type_evaluation
import literal
import newtype
import rename
import rename_all
import simple
import skip
import tomlfile
import type_datetime
import type_decimal
import union
import union_tagging
import user_exception
import yamlfile

PY310 = sys.version_info[:3] >= (3, 10, 0)


def run_all():
    run(any)
    run(simple)
    run(newtype)
    run(collection)
    run(default)
    run(env)
    run(flatten)
    run(jsonfile)
    run(rename)
    run(rename_all)
    run(skip)
    run(tomlfile)
    run(yamlfile)
    run(union)
    run(custom_class_serializer)
    run(custom_field_serializer)
    run(forward_reference)
    run(type_decimal)
    run(type_datetime)
    run(union_tagging)
    run(generics)
    run(lazy_type_evaluation)
    run(literal)
    run(user_exception)
    if PY310:
        import union_operator

        run(union_operator)


def run(module):
    print('-----------------')
    print(f'running {module.__name__}')
    module.main()


if __name__ == '__main__':
    try:
        run_all()
    except Exception:
        sys.exit(1)
