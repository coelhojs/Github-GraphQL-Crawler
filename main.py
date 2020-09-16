import time
import requests
from datetime import datetime
from queries import queries
from json import dump
from json import loads


def fetch(query, json, headers):
    request = requests.post(
        'https://api.github.com/graphql', json=json, headers=headers)
    if request.status_code == 200:
        return request.json()

    time.sleep(1)

    return fetch(query, json, headers)


def run(query, page_limit=10):
    token = '' #INSERT TOKEN
    headers = {"Authorization": "Bearer " + token}
    finalQuery = query.replace("{AFTER}", "")
    json = {"query": finalQuery, "variables": {}}

    total_pages = 1

    result = fetch(query, json, headers)

    nodes = result['data']['search']['nodes']
    next_page = result["data"]["search"]["pageInfo"]["hasNextPage"]

    while (next_page and total_pages < page_limit):
        total_pages += 1
        cursor = result["data"]["search"]["pageInfo"]["endCursor"]
        next_query = query
        json["query"] = next_query.replace(
            "{AFTER}", ", after: \"%s\"" % cursor)
        result = fetch(query, json, headers)
        nodes += result['data']['search']['nodes']
        next_page = result["data"]["search"]["pageInfo"]["hasNextPage"]

    return nodes


def RQ1():
    try:
        query = queries[0]

        nodes = run(query)

        filename = "RQ1.csv"

        with open(filename, 'a') as the_file:
            the_file.write('nameWithOwner;stargazersTotalCount;yearsOld\n')

        for node in nodes:
            years_old = int((datetime.now(
            ) - datetime.strptime(node['createdAt'], '%Y-%m-%dT%H:%M:%SZ')).days / 365)

            with open(filename, 'a') as the_file:
                the_file.write("%s;%s;%s\n" % (
                    node['nameWithOwner'], node['stargazers']['totalCount'], years_old))
    except Exception as ex:
        print(ex)
        pass


def RQ2():
    try:
        query = queries[1]

        nodes = run(query, 100)

        filename = "RQ2.csv"

        with open(filename, 'a') as the_file:
            the_file.write(
                'nameWithOwner;totalRequests;acceptedPullRequests\n')

        for node in nodes:
            aceitas = node['ACCEPTED_PRs']['totalCount']
            total = node['TOTAL_PRs']['totalCount']

            with open(filename, 'a') as the_file:
                the_file.write("%s;%s;%s\n" % (
                    node['nameWithOwner'], total, aceitas))
    except Exception as ex:
        print(ex)
        pass


def RQ3():
    try:
        query = queries[2]

        nodes = run(query)

        filename = "RQ3.csv"

        with open(filename, 'a') as the_file:
            the_file.write('nameWithOwner;stargazers;totalReleases\n')

        for node in nodes:
            with open(filename, 'a') as the_file:
                the_file.write("%s;%s;%s\n" % (
                    node['nameWithOwner'], node['stargazers']['totalCount'], node['releases']['totalCount']))
    except Exception as ex:
        print(ex)
        pass


def RQ4():
    try:
        query = queries[3]

        nodes = run(query)

        filename = "RQ4.csv"

        with open(filename, 'a') as the_file:
            the_file.write('nameWithOwner;stargazers;daysSinceLastUpdate\n')

        for node in nodes:
            daysSinceLastUpdate = (
                datetime.utcnow() - datetime.strptime(node['updatedAt'], '%Y-%m-%dT%H:%M:%SZ')).days

            if (daysSinceLastUpdate < 0):
                daysSinceLastUpdate = 0

            with open(filename, 'a') as the_file:
                the_file.write("%s;%s;%s\n" % (
                    node['nameWithOwner'], node['stargazers']['totalCount'], daysSinceLastUpdate))
    except Exception as ex:
        print(ex)
        pass


def RQ5():
    try:
        query = queries[4]

        nodes = run(query)

        filename = "RQ5.csv"

        with open(filename, 'a') as the_file:
            the_file.write('nameWithOwner;stargazers;mostUsedLanguage\n')

        for node in nodes:
            if (len(node['languages']['edges']) > 0):
                top_language = node['languages']['edges'][0]['node']['name']
            else:
                top_language = "NA"

            with open(filename, 'a') as the_file:
                the_file.write("%s;%s;%s\n" % (
                    node['nameWithOwner'], node['stargazers']['totalCount'], top_language))
    except Exception as ex:
        print(ex)
        pass


def RQ6():
    try:
        query = queries[5]

        nodes = run(query, 11)

        filename = "RQ6.csv"

        with open(filename, 'a') as the_file:
            the_file.write(
                'nameWithOwner;stargazers;totalIssues;closedIssues;ratio\n')

        for node in nodes:
            fechadas = node['ISSUES_FECHADAS']['totalCount']
            total = node['TOTAL_ISSUES']['totalCount']
            if fechadas != 0 and total != 0:
                ratio = "{:.2f}".format(
                    (fechadas / total) * 100).replace('.', ',')
            else:
                ratio = 'NA'

            with open(filename, 'a') as the_file:
                the_file.write("%s;%s;%s;%s;%s\n" % (
                    node['nameWithOwner'], node['stargazers']['totalCount'], total, fechadas, ratio))
    except Exception as ex:
        print(ex)
        pass


RQ1()
RQ2()
RQ3()
RQ4()
RQ5()
RQ6()