from django.core.management.base import BaseCommand
from django.conf import settings

from qa.services.access import get_connection

import pandas as pd
from sqlalchemy import create_engine


class Command(BaseCommand):
    help = "Sync Access tables to SQLite"

    def handle(self, *args, **kwargs):

        self.stdout.write("Connecting to Access...")

        conn = get_connection(
            settings.ACCESS_DB_PATH,
            settings.ACCESS_DB_PASSWORD,
        )

        tables = [
            "PDD Reference Data",
            "PDD Session",
            "PDD Tolerances",
            "PDD Results",
        ]

        sqlite_engine = create_engine(f"sqlite:///{settings.BASE_DIR / 'db.sqlite3'}")

        for table in tables:

            self.stdout.write(f"Importing {table}...")

            df = pd.read_sql(f"SELECT * FROM [{table}]", conn)

            table_name = table.lower().replace(" ", "_")

            df.to_sql(
                table_name,
                sqlite_engine,
                if_exists="replace",
                index=False,
            )

            self.stdout.write(self.style.SUCCESS(f"{table}: {len(df)} rows"))

        conn.close()

        self.stdout.write(self.style.SUCCESS("Sync completed successfully"))
