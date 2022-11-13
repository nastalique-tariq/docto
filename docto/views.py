import json
from django.http import HttpResponse
from models.disease_prediction import disease_prediction
from models.recommender import recommender


def index(request):
    return HttpResponse("Docto API running...")


def doctor_recommendation(request, id):
    res = recommender.recommend_doctor(id)
    return HttpResponse(json.dumps(res), content_type="application/json")


def symptoms_selection(request, id):
    id_ = id.split('-')
    id_.extend([-1 for _ in range(17 - len(id_))])
    res = disease_prediction.predict(id_)
    return HttpResponse(json.dumps({"result": res[0]}), content_type="application/json")
