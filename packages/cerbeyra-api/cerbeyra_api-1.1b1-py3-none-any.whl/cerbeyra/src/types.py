from enum import Enum


class AssetTypes(Enum):
    NETWORK = 'network'
    WEB = 'web'
    DOMAIN = 'domain'


class Perimeters(Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'


class ScanStatus(Enum):
    SCHEDULED = 'Scheduled'
    RUNNING = 'Running'
    STOP = 'Stop'
    REQUESTED = 'Requested'
    COMPLETED = 'Completed'
    DONE = 'Done'
    EMPTY = 'Empty'
    ERROR = 'Error'
    STOPPED = 'Stopped'


class IoTStatus(Enum):
    ALIVE = 'ALIVE'
    WARNING = 'WARNING'
    DANGER = 'DANGER'


class NetworkReportFields(Enum):
    asset = 'asset'
    host = 'host'
    hostname = 'hostname'
    vulnerability = 'vulnerability'
    description = 'description'
    threat = 'threat'
    solution = 'solution'
    vuln_id = 'vuln_id'
    last_detection = 'last_detection'
    first_detection = 'first_detection'
    protocol = 'protocol'
    port = 'port'
    cvss = 'cvss'
    summary = 'summary'
    insight = 'insight'
    impact = 'impact'
    affected = 'affected'
    references = 'references'


class WebReportFields(Enum):
    asset = 'asset'
    host = 'host'
    hostname = 'hostname'
    vulnerability = 'vulnerability'
    description = 'description'
    threat = 'threat'
    solution = 'solution'
    vuln_id = 'vuln_id'
    last_detection = 'last_detection'
    first_detection = 'first_detection'
    other = 'other'
    param = 'param'
    attack = 'attack'
    evidence = 'evidence'
    response = 'response'
    request = 'request',
    family = 'family'
    url = 'url'
    method = 'method'


class ThreatLevels(Enum):
    high = 'high'
    medium = 'medium'
    low = 'low'
    log = 'log'


class DetailLevel(Enum):
    BASE = 1
    DETAILED = 2
    THOROUGH = 3
