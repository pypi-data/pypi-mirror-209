from cerbeyra import CerbeyraApi
from cerbeyra.exceptions import UnauthorizedApiException
from cerbeyra.src import BaseApi

# endpoint = "http://local.cloudscan.vola.it"
endpoint = "https://pre-areaclienti.cerbeyra.com"
cc = BaseApi(username='nicola.dipietro@vola.it', password='Necciobao91!', endpoint=endpoint)

with cc:
    print(cc.get_cerbeyra_index())
    pps = cc.get_probes()
    for p in pps:
        print(p)

    # report = cc.get_report_network()
    # print(report.get_distinct_hosts())
    # print(cc.get_all_assets().length)

    try:

        for cli in cc.get_all_clients(active=True):
            print(f"{cli.client_id} -> {cli.company}")
    except UnauthorizedApiException:
        pass

    net = cc.get_network_vulns()
    print(net.group_by_threat(aggr=True))

    trend = cc.get_technical_info()
    print(trend.history)
    print(trend.index)
    print(trend.vulnerability_assessment)

    for scan in cc.get_network_scans():
        print(scan.vulns)
