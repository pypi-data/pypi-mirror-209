import sys

from scandal import connect


def main(org, project, sql):
    with connect(org=org, project=project) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        if cursor.rowcount() > 0:
            print(cursor.fetchall())
        cursor.close()


if __name__ == "__main__":
    org = sys.argv[1] if len(sys.argv) > 1 else "fulcrum"
    project = sys.argv[2] if len(sys.argv) > 2 else "loyal-road-382017"
    sql = sys.argv[3] if len(sys.argv) > 3 else "SELECT 1"
    main(org, project, sql)
