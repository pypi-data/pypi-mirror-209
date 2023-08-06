from datetime import datetime

Y_M_D = "%Y-%m-%d"


def normalize_date(date: str | datetime) -> str:
    return date.strftime(Y_M_D) if type(date) == datetime else date

def clean_column_ids(column_ids: list, prefix: str) -> list[int]:
    unique_ids = set(column_ids)

    clean_ids: list[int] = []
    for i in unique_ids:
        if str(i).isdigit():
            clean_ids.append(int(i))
            continue
        parts = str(i).split('_')
        if all(str(part).isdigit() for part in parts):
            clean_ids.append(int(parts[0]))
            continue
        if str(i).startswith(prefix):
            index = i.find(prefix) + len(prefix)
            id_raw = str(i[index:])
            raw_id = int(id_raw.split('_')[0])
            clean_ids.append(raw_id)
    return list(set(clean_ids))