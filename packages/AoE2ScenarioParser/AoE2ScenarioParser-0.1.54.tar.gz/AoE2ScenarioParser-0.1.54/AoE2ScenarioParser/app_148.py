from AoE2ScenarioParser.local_config import folder_de
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

filename = "p2-map-initially"
scenario2 = AoE2DEScenario.from_file(f"{folder_de}{filename}.aoe2scenario")

filename = "p8-map-initially"
scenario8 = AoE2DEScenario.from_file(f"{folder_de}{filename}.aoe2scenario")

scenario2._debug_compare(other=scenario8)
