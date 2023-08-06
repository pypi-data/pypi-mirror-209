import shutil
from tempfile import NamedTemporaryFile


def stream_response_to_temp_file(response):
    tmp_file = NamedTemporaryFile(delete=False)
    with response:
        with open(tmp_file.name, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        return tmp_file.name
