import pymongo
from flask import Blueprint, jsonify, request
import concatParts as cp
import concatNewses as cn
import getSelectors as gs

apis = Blueprint(__name__, 'apis')

def is_total_selected(selected_date, selected_keyword, selected_company):

    if selected_date == "total":
        is_date_total = True
    else:
        is_date_total = False

    if selected_keyword == "total":
        is_keyword_total = True
    else:
        is_keyword_total = False

    if selected_company == "total":
        is_company_total = True
    else:
        is_company_total = False

    return {
        "date": is_date_total,
        "keyword": is_keyword_total,
        "company": is_company_total
    }


@apis.route('/api/statistics', methods=["GET"])
def statistics():
    selected_date = request.args.get("date")
    selected_keyword = request.args.get("keyword")
    selected_company = request.args.get("company")

    is_total = is_total_selected(selected_date, selected_keyword, selected_company)

    if is_total["date"]:
        if is_total["keyword"]:
            if is_total["company"]:
                return jsonify(cp.date_total_keyword_total_company_total())
            else:
                return jsonify(cp.date_total_keyword_total_company_specific(selected_company))
        else:
            if is_total["company"]:
                return jsonify(cp.date_total_keyword_specific_company_total(selected_keyword))
            else:
                return jsonify(cp.date_total_keyword_specific_company_specific(selected_keyword, selected_company))
    else:
        if is_total["keyword"]:
            if is_total["company"]:
                return jsonify(cp.date_specific_keyword_total_company_total(selected_date))
            else:
                return jsonify(cp.date_specific_keyword_total_company_specific(selected_date, selected_company))
        else:
            if is_total["company"]:
                return jsonify(cp.date_specific_keyword_specific_company_total(selected_date, selected_keyword))
            else:
                return jsonify(cp.date_specific_keyword_specific_company_specific(selected_date, selected_keyword, selected_company))



@apis.route('/api/newses', methods=["GET"])
def news_list():
    selected_date = request.args.get("date")
    selected_keyword = request.args.get("keyword")
    selected_company = request.args.get("company")

    is_total = is_total_selected(selected_date, selected_keyword, selected_company)

    if is_total["date"]:
        if is_total["keyword"]:
            if is_total["company"]:
                return jsonify(cn.date_total_keyword_total_company_total())
            else:
                return jsonify(cn.date_total_keyword_total_company_specific(selected_company))
        else:
            if is_total["company"]:
                return jsonify(cn.date_total_keyword_specific_company_total(selected_keyword))
            else:
                return jsonify(cn.date_total_keyword_specific_company_specific(selected_keyword, selected_company))
    else:
        if is_total["keyword"]:
            if is_total["company"]:
                return jsonify(cn.date_specific_keyword_total_company_total(selected_date))
            else:
                return jsonify(cn.date_specific_keyword_total_company_specific(selected_date, selected_company))
        else:
            if is_total["company"]:
                return jsonify(cn.date_specific_keyword_specific_company_total(selected_date, selected_keyword))
            else:
                return jsonify(cn.date_specific_keyword_specific_company_specific(selected_date, selected_keyword, selected_company))

@apis.route('/api/selectors', methods=["GET"])
def selectors():
    selectors = gs.getSelectors()
    result = {}
    for key in selectors.keys():
        temp = []
        for selector in selectors[key].keys():
            temp.append(selector)
        result[key] = temp
    return jsonify(result)


