from boggle import BoggleBoard


def main():
    boggle = BoggleBoard()
    boggle.test_case_one()
    guess = boggle.get_current_guess()
    print(boggle.check_guess_validity(guess))


if __name__ == "__main__":
    main()
