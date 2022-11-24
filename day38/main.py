import nix, sheetly


def main():
    data = nix.get_ex_dur_cal()

    sheetly.post(data)


if __name__ == "__main__":
    main()
