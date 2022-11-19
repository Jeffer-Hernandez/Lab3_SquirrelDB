import json
from google.cloud import bigquery
from django.shortcuts import render

client = bigquery.Client()

def home(request):

    return render(request, "home.html")
    
def view_all(request):
    context = {}
    row_dict = {}
    res = []
    query_job = client.query(
        """
        SELECT *
        FROM `cisc3140-368419.Squirrel_Sightings.SquirrelDB`
        
        """
    )
    results = query_job.result()  # Waits for job to complete.
    for row in results:
        row_dict["ID"] = row["ID"]
        row_dict["Above_Ground"] = row["Above_Ground"]
        row_dict["Specific_Location"] = row["Specific_Location"]
        row_dict["Running"] = row["Running"]
        row_dict["Chasing"] = row["Chasing"]
        row_dict["Climbing"] = row["Climbing"]
        row_dict["Eating"] = row["Eating"]
        row_dict["Foraging"] = row["Foraging"]
        row_dict["Kuks"] = row["Kuks"]
        row_dict["Quaas"] = row["Quaas"]
        row_dict["Moans"] = row["Moans"]
        row_dict["Tail_Flags"] = row["Tail_Flags"]
        row_dict["Tail_Twitch"] = row["Tail_Twitch"]
        row_dict["Approach"] = row["Approach"]
        row_dict["Runs_Away"] = row["Runs_Away"]
        row_dict["Indifferent"] = row["Indifferent"]
        row_dict["Hectare"] = row["Hectare"]
        row_dict["Date"] = row["Date"]
        row_dict["Shift"] = row["Shift"]
        row_dict["Age"] = row["Age"]
        row_dict["Primary_Color"] = row["Primary_Color"]
        row_dict["Highlight_Color"] = row["Highlight_Color"]
        row_dict["Special_Notes"] = row["Special_Notes"]
        row_copy = row_dict.copy()
        res.append(row_copy)
    
    print(res[2])
    context["results"] = res
    # print(result)
    # print(results.num_results)
    return render(request, "results.html", context)