from src.models.equipment import Equipment


def generate_equipment_table(service_parameters):
    equipment = []
    for service in service_parameters:
        equipment.append(
            Equipment(name=service["part"], type="część", cost=service["part_cost"])
        )
    return equipment
