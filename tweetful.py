import authorization

def main():
    """ Main function """
    auth = authorization.authorize()

    response = requests.get(TIMELINE_URL, auth=auth)
    print response.json()

if __name__ == "__main__":
    main()

