#!/usr/bin/env python3
# Copyright 2021 BHG [bw.org]
# as of 2021-04-07 bw

import mysql.connector as mysql


def main():
    db = mysql.connect(host = "localhost",user="root", password = "Constantinople1452")
    cur = db.cursor()

    cur.execute("SELECT VERSION()")
    version = cur.fetchone()[0]
    print(f"MySQL version {version}")

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
