import api


def main():

    keyword = input("Please enter the keyword : ")
    results = api.search_by_keyword(keyword)
    number_of_episodes = 0
    for r in results:
        if r.category == 'Episode':
            number_of_episodes += 1
        print(f'{r.title } has url {r.url}')
    print(f'The number of results : {len(results)}')
    print(f'The number of episodes are {number_of_episodes}')


if __name__ == '__main__':

    main()

