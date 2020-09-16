queries = ["""
query RQ1 {
    search(query: "stars:>10000", type: REPOSITORY, first: 100, {AFTER}) {
        pageInfo {
            hasNextPage
            endCursor
        }
        nodes {
            ... on Repository {
                nameWithOwner
                createdAt
                stargazers {
                    totalCount
                }
            }  
        }
    }
}
""",
           """
query RQ2 {
    search(query: "stars:>10000", type: REPOSITORY, first: 10, {AFTER}) {
        pageInfo {
            hasNextPage
            endCursor
        }
        nodes {
            ... on Repository {
                nameWithOwner
                url
                createdAt
                stargazers {
                    totalCount
                }
                TOTAL_PRs: pullRequests {
                    totalCount
                }
                ACCEPTED_PRs: pullRequests(states: CLOSED) {
                    totalCount
                }   
            }
        }
    }
}
""",
           """
query RQ3 {
    search(query: "stars:>10000", type: REPOSITORY, first: 100, {AFTER}) {
        pageInfo {
            hasNextPage
            endCursor
        }    
        nodes {
            ... on Repository {
                nameWithOwner
                createdAt
                stargazers {
                    totalCount
                }
                releases {
                    totalCount
                }
            }
        }
    }
}
""",
           """
query RQ4 {
  search(query: "stars:>10000", type: REPOSITORY, first: 100, {AFTER}) {
    pageInfo {
            hasNextPage
            endCursor
    }
    nodes {
        ... on Repository {
                nameWithOwner
                createdAt
                stargazers {
                    totalCount
                }
                updatedAt
            }
        }
    }
}
""",
           """
query RQ5 {
    search(query: "stars:>10000", type: REPOSITORY, first: 100, {AFTER}) {
        pageInfo {
                hasNextPage
                endCursor
        }
        nodes {
            ... on Repository {
                nameWithOwner
                stargazers {
                    totalCount
                }
                languages(orderBy: {field: SIZE, direction: DESC}, first: 1) {
                    edges {
                        node {
                            name
                        }
                    }
                }
            }
        }
    }
}
""",
           """
query RQ6 {
    search(query:"stars:>10000 sort:stars",type:REPOSITORY, first:100, {AFTER}) {
        pageInfo {
                hasNextPage
                endCursor
        }
        nodes {
            ... on Repository {
                nameWithOwner
                createdAt
                stargazers {
                    totalCount
                }
                TOTAL_ISSUES: issues {
                    totalCount
                }
                ISSUES_FECHADAS: issues(states: CLOSED) {
                    totalCount
                }
            }
        }
    }
}
"""]
