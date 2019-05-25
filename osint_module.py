import requests




def subdomain(query):
    response=requests.get(query)
    print("\n---SUB DOMAINS---\n")
    print(response.text)
    print("\n----------------\n")


def dnslookup(query):
    response=requests.get(query)
    print("\n---DNS LOOKUP---\n")
    print(response.text)
    print("\n----------------\n")


def reversedns(query):
    response=requests.get(query)
    print("\n---REVERSE DNS---\n")
    print(response.text)
    print("\n----------------\n")


def zonetransfer(query):
    response=requests.get(query)
    print("\n---ZONE TRANSFER---\n")
    print(response.text)
    print("\n----------------\n")


def reverseip(query):
    response=requests.get(query)
    print("\n---REVERSE IP LOOKUP---\n")
    print(response.text)
    print("\n----------------\n")
