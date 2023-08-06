from dotenv import load_dotenv
import os
from cerbeyra import CerbeyraApi
from cerbeyra.src import BaseApi
from cerbeyra.src.types import Perimeters, AssetTypes, NetworkReportFields, WebReportFields, IoTStatus

load_dotenv()

username_ = 'maremma@vola.it'  # os.getenv('CERBEYRA_EMAIL')
password_ = 'Asdfg2023!'  # os.getenv('CERBEYRA_PASSWORD')

# with BaseApi(username_, password_, endpoint="http://local.cloudscan.vola.it") as cerbeyra_client:
#     cerb = cerbeyra_client.get_cerbeyra_index()
#     print(cerb)
#     net_repo = cerbeyra_client.get_report_network(columns=[NetworkReportFields.host.value])
#     print(net_repo.get_distinct_hosts())
#     exit(1)
#     assets = cerbeyra_client.get_all_assets(client_id=1)
#     assets = assets.filter_by_type(AssetTypes.NETWORK)
#     print(type(assets))
#     groupy = assets.group_by_perimeter()
#     print({k: type(groupy[k]) for k in groupy})
#
#     vulns = cerbeyra_client.get_network_vulns(client_id=1)
#     groups = vulns.group_by_threat()
#     print({k: type(groups[k]) for k in groups})
#     for threat in groups:
#         col = groups[threat]
#         col.save_csv(f"{threat}.csv")

username__ = os.getenv('CERBEYRA_EMAIL')
password__ = os.getenv('CERBEYRA_PASSWORD')

# OLD API
with CerbeyraApi(username__, password__) as cerbeyra_api:
    # Cerbeyra Index
    index = cerbeyra_api.get_cerbeyra_index()
    print(index)
    # Client
    clients = cerbeyra_api.get_all_clients(active=True)
    print("Companies")
    print(", ".join([c.company for c in clients]))
    # Probes
    probes = cerbeyra_api.get_all_probes(status=IoTStatus.DANGER.value)
    print("Danger Probes:")
    for p in probes:
        print(f"({p.probe_id}) {p.name}")
    # Sensor
    sensors = cerbeyra_api.get_all_sensors()
    print("Sensors")
    for s in sensors:
        print(s.name)

    # Report Network
    net_repo = cerbeyra_api.get_report_network()
    print(net_repo.get_distinct_hosts())
    # Report Web
    web_repo = cerbeyra_api.get_report_web()
    print(f"Total Urls: {len(web_repo.get_distinct_urls())}")
