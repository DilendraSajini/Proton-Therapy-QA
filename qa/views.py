from django.shortcuts import render
from django.db import connection


def dashboard(request):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT Energy,
               AVG(PTPR)
        FROM pdd_results
        GROUP BY Energy
        ORDER BY Energy
    """)

    rows = cursor.fetchall()

    labels = [str(row[0]) for row in rows]
    values = [float(row[1]) for row in rows]

    return render(
        request,
        "qa/dashboard.html",
        {
            "labels": labels,
            "values": values,
        },
    )
