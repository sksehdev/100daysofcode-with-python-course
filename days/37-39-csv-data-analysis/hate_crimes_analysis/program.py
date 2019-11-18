from research import DataAnalysis

def main():
    research = DataAnalysis("hate_crimes.csv")
    highest_median_income = research.highest_median_income()
    print("States with highest medium income ")
    for num, row in enumerate(highest_median_income[:5]):
        print(f'{num + 1} . {row.state} has mean  household income of {row.median_household_income}')

    highest_trump_votes = research.highest_trump_votes()
    print("States with highest Trump vote ")
    for num, row in enumerate(highest_trump_votes[:5]):
        print(f'{num + 1} . {row.state} : {row.share_voters_voted_trump}')

    highest_white_poverty = research.highest_white_poor()
    print("States with highest White poverty  ")
    for num, row in enumerate(highest_white_poverty[:5]):
        print(f'{num + 1} . {row.state} : {row.share_white_poverty}')

    highest_avg_hatecrime = research.highest_avg_hatecrime()
    print("States with highest hate crime  ")
    for num, row in enumerate(highest_avg_hatecrime[:5]):
        print(f'{num + 1} . {row.state} : {row.avg_hatecrimes_per_100k_fbi}')

    #print(highest_median_income)










if __name__ == "__main__":
    main()