from advent.plan_importer import PlanImporter

plan_importer = PlanImporter()
plan_importer.read_file('./files/day5_input')
plan_importer.plan.execute()
print('Top crates:', plan_importer.plan.get_top_crates())

plan_importer = PlanImporter()
plan_importer.read_file('./files/day5_input')
plan_importer.plan.execute_contain_order()
print('Top crates when keeping order:', plan_importer.plan.get_top_crates())
