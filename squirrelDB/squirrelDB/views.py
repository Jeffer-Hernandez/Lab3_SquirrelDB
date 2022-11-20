import json
from google.cloud import bigquery
from django.shortcuts import render, redirect

client = bigquery.Client()

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
    results = query_job.result()  
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

    context["results"] = res

    return render(request, "results.html", context)

def create(request):
    if request.method=="GET":
        context = {}
        return render(request, "create.html", context) 
    elif request.method=="POST":
        # if post save in db and send of to view all, including the newest entry
        id = request.POST.get("ID")
        Above_Ground = request.POST.get("Above_Ground")
        Specific_Location = request.POST.get("Specific_Location")
        Running = request.POST.get("Running")
        Chasing = request.POST.get("Chasing")
        Climbing = request.POST.get("Climbing")
        Eating = request.POST.get("Eating")
        Foraging = request.POST.get("Foraging")
        Kuks = request.POST.get("Kuks")
        Quaas = request.POST.get("Quaas")
        Moans = request.POST.get("Moans")
        Tail_Flags = request.POST.get("Tail_Flags")
        Tail_Twitch = request.POST.get("Tail_Twitch")
        Approach = request.POST.get("Approach")
        Runs_Away = request.POST.get("Runs_Away")
        Indifferent = request.POST.get("Indifferent")
        Hectare = request.POST.get("Hectare")
        Date = request.POST.get("Date")
        Shift = request.POST.get("Shift")
        Age = request.POST.get("Age")
        Primary_Color = request.POST.get("Primary_Color")
        Highlight_Color = request.POST.get("Highlight_Color")
        Special_Notes = request.POST.get("Special_Notes")

        rows_to_insert = [
            {   "id": id,
                "Above_Ground": Above_Ground, 
                "specific_location": Specific_Location ,
                "running": Running,
                "chasing": Chasing,
                "climbing": Climbing,
                "eating": Eating,
                "foraging": Foraging,
                "kuks": Kuks,
                "quaas": Quaas,
                "moans": Moans,
                "tail_flags": Tail_Flags,
                "tail_twitch": Tail_Twitch,
                "approach": Approach,
                "runs_away": Runs_Away,
                "indifferent": Indifferent,
                "hectare": Hectare,
                "date": Date,
                "shift": Shift,
                "age": Age,
                "primary_color": Primary_Color,
                "highlight_color": Highlight_Color,
                "special_notes": Special_Notes
            }
        ]

        errors = client.insert_rows_json(
            "cisc3140-368419.Squirrel_Sightings.SquirrelDB", rows_to_insert, row_ids=[None] * len(rows_to_insert)
        ) 

        if errors == []:
            print("New rows have been added.")
        else:
            print("Encountered errors while inserting rows: {}".format(errors))
        return redirect('view-all')

def delete(request):
    if request.method=="GET":
        return render(request, "delete.html") 
    elif request.method=="POST":
        print(request.POST.get("ID"))
        id = request.POST.get("ID")
        query = """
        DELETE FROM `cisc3140-368419.Squirrel_Sightings.SquirrelDB` WHERE ID = @id;
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("id", "INT64", id),
            ]
        )
        
        result = client.query(query, job_config=job_config) 
        print(result.result())
        return view_all(request)

def update(request):
    if request.method=="GET":
        return render(request, "delete.html") 
    elif request.method=="POST" and "Above_Ground" not in request.POST:
        print(request.POST)
        id = request.POST.get("ID")
        context = {}
        row_dict = {}
        query = """
        SELECT *
        FROM `cisc3140-368419.Squirrel_Sightings.SquirrelDB`
        WHERE ID = @id;
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("id", "INTEGER", id),
            ]
        )
        results = client.query(query, job_config=job_config) 
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
            context["entity"] = row_dict
        return render(request, "update.html", context)   
    elif request.method=="POST" and "Above_Ground" in request.POST:
        id = request.POST.get("ID")
        Above_Ground = request.POST.get("Above_Ground")
        Specific_Location = request.POST.get("Specific_Location")
        Running = request.POST.get("Running")
        Chasing = request.POST.get("Chasing")
        Climbing = request.POST.get("Climbing")
        Eating = request.POST.get("Eating")
        Foraging = request.POST.get("Foraging")
        Kuks = request.POST.get("Kuks")
        Quaas = request.POST.get("Quaas")
        Moans = request.POST.get("Moans")
        Tail_Flags = request.POST.get("Tail_Flags")
        Tail_Twitch = request.POST.get("Tail_Twitch")
        Approach = request.POST.get("Approach")
        Runs_Away = request.POST.get("Runs_Away")
        Indifferent = request.POST.get("Indifferent")
        Hectare = request.POST.get("Hectare")
        Date = request.POST.get("Date")
        Shift = request.POST.get("Shift")
        Age = request.POST.get("Age")
        Primary_Color = request.POST.get("Primary_Color")
        Highlight_Color = request.POST.get("Highlight_Color")
        Special_Notes = request.POST.get("Special_Notes")

        query = """
            UPDATE "cisc3140-368419.Squirrel_Sightings.SquirrelDB"
            SET 
                Above_Ground = @Above_Ground,
                Specific_Location = @Specific_Location,
                Running = @Running,
                Chasing = @Chasing,
                Climbing = @Climbing,
                Eating = @Eating,
                Foraging = @Foraging,
                Kuks = @Kuks,
                Quaas = @Quaas,
                Moans = @Moans,
                Tail_Flags = @Tail_Flags,
                Tail_Twitch = @Tail_Twitch,
                Approach = @Approach,
                Runs_Away = @Runs_Away,
                Indifferent = @Indifferent,
                Hectare = @Hectare,
                Date = @Date,
                Shift = @Shift,
                Age = @Age,
                Primary_Color = @Primary_Color,
                Highlight_Color = @Highlight_Color,
                Special_Notes = @Special_Notes
            WHERE ID = @id;
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("id", "INT64", id),
                bigquery.ScalarQueryParameter("Above_Ground", "STRING", Above_Ground),
                bigquery.ScalarQueryParameter("Specific_Location", "STRING", Specific_Location),
                bigquery.ScalarQueryParameter("Running", "BOOL", Running),
                bigquery.ScalarQueryParameter("Chasing", "BOOL", Chasing),
                bigquery.ScalarQueryParameter("Climbing", "BOOL", Climbing),
                bigquery.ScalarQueryParameter("Eating", "BOOL", Eating),
                bigquery.ScalarQueryParameter("Foraging", "BOOL", Foraging),
                bigquery.ScalarQueryParameter("Kuks", "BOOL", Kuks),
                bigquery.ScalarQueryParameter("Quaas", "BOOL", Quaas),
                bigquery.ScalarQueryParameter("Moans", "BOOL", Moans),
                bigquery.ScalarQueryParameter("Tail_Flags", "BOOL", Tail_Flags),
                bigquery.ScalarQueryParameter("Tail_Twitch", "BOOL", Tail_Twitch),
                bigquery.ScalarQueryParameter("Approach", "BOOL", Approach),
                bigquery.ScalarQueryParameter("Runs_Away", "BOOL", Runs_Away),
                bigquery.ScalarQueryParameter("Indifferent", "BOOL", Indifferent),
                bigquery.ScalarQueryParameter("Hectare", "INT64", Hectare),
                bigquery.ScalarQueryParameter("Date", "INT64", Date),
                bigquery.ScalarQueryParameter("Shift", "DATE", Shift),
                bigquery.ScalarQueryParameter("Age", "STRING", Age),
                bigquery.ScalarQueryParameter("Primary_Color", "STRING", Primary_Color),
                bigquery.ScalarQueryParameter("Highlight_Color", "STRING", Highlight_Color),
                bigquery.ScalarQueryParameter("Special_Notes", "STRING", Special_Notes),
            ]
        )
        client.query(query, job_config=job_config) 
        return redirect('view-all')
