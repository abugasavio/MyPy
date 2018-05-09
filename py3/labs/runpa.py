#from py3mt import force, Mario
from py3pa import force, Mario
from pyannotate_runtime import collect_types


def test_pa():
    force(mass=10, acceleration=9.8)
    Mario().speed()


collect_types.init_types_collection()
with collect_types.collect():
    test_pa()
collect_types.dump_stats('type_info.json')
