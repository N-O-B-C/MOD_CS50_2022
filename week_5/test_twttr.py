from twttr import vowel_omittion


def main():
    vowel_omittion()


def test_twttr():
    assert vowel_omittion("twitter") == "twttr"
    

if __name__ == "__main__":
    main()